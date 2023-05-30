import os

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from data_kvant_doc.settings import MEDIA_ROOT
from users.forms import User

from .forms import DocumentForm, EventForm, ReportForm, SigDocForm
from .models import Document, Event, Report, SigDoc


def doc_list(request):
    is_sign_doc = []
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.author = request.user
            newdoc.save()
            messages.success(request, 'Документ успешно добавлен.')
            return redirect('doc_list')
        messages.error(request, 'Что-то пошло не так :(')
        return render(request, 'new_doc.html', context={'form': form})
    form = DocumentForm()
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    documents = list(reversed(Document.objects.all()))

    paginator = Paginator(documents, 8)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {'documents': reversed(documents), 'form': form, 'user': request.user, 'perm': permissions, 'page': page,
               'posts': posts, "paginator": paginator, "SigDoc": SigDoc}
    return render(request, 'list.html', context)


def signature(request, document_id):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    document = get_object_or_404(Document, id=document_id)
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = SigDocForm(request.POST, request.FILES)
        if form.is_valid():
            newsigdoc = form.save(commit=False)
            newsigdoc.signaturer = request.user
            newsigdoc.doc = document
            newsigdoc.save()

            document.signature.add(user)
            document.save()
            messages.success(request, 'Документ успешно подписан.')
            return redirect('doc_list')
        messages.error(request, 'Что-то пошло не так :(')
        return redirect(doc_list)
    form = SigDocForm()
    context = {'form': form, 'user': request.user, 'perm': permissions, 'document_id': document_id}
    return render(request, "signature.html", context)


def new_doc(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    form = DocumentForm(request.POST, request.FILES)

    context = {'form': form, 'perm': permissions}
    return render(request, 'new_doc.html', context)


def events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.author = request.user
            new_event.save()
            messages.success(request, 'Мероприятие успешно добавлено.')
            return redirect('events')
        messages.error(request, 'Что-то пошло не так :(')
        return render(request, 'new_event.html', context={'form': form})
    form = EventForm()
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    events = list(reversed(Event.objects.all()))
    paginator = Paginator(events, 7)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'events.html', context={
        'perm': permissions, 'events': reversed(events),
        'form': form, 'posts': posts, "paginator": paginator
    })


def new_event(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    form = EventForm(request.POST, request.FILES)

    context = {'form': form, 'perm': permissions}
    return render(request, 'new_event.html', context)


def event_one(request, event_id):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0

    event = get_object_or_404(Event, id=event_id)

    context = {'perm': permissions, "event": event}
    return render(request, 'event_one.html', context)


def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if document.author == request.user:
        os.remove(document.file.path)
        document.delete()
        return redirect('doc_list')
    else:
        return redirect('doc_list')


def check_sig(request, document_id):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    document = get_object_or_404(Document, id=document_id)
    SigDocum = SigDoc.objects.all()
    context = {"document": document, "SigDocum": SigDocum, "perm": permissions}
    return render(request, "check_sig.html", context)


def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.author == request.user:
        event.delete()
        return redirect('events')
    else:
        return redirect('events')


def my_doc(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0

    documents = []
    for document in Document.objects.all():
        if document.author == request.user:
            documents.append(document)

    documents = list(reversed(documents))
    paginator = Paginator(documents, 8)
    page = request.GET.get('page')
    print(paginator.num_pages)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'documents': reversed(documents),
        'perm': permissions,
        'posts': posts,
        'paginator': paginator
    }
    return render(request, 'my_documents.html', context)


def notifications(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    context = {'perm': permissions}
    return render(request, 'notifications.html', context)


def search_list(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    letters = request.GET.get('q').lower()
    result = []
    for word in Document.objects.all():
        name = word.name.lower()
        if len(letters) == 0:
            break
        if name.startswith(letters):
            result.append(word)
        elif len(name) == len(letters):
            errors = 0
            for i in range(len(name)):
                if word.file.name[i] != letters[i]:
                    errors += 1
            if len(letters) > 3:
                if errors <= 2:
                    result.append(word)

        elif len(name) >= len(letters):
            errors = 0
            for i in range(len(letters)):
                if letters[i] != word.file.name[i]:
                    errors += 1
            if len(letters) > 3:
                if errors <= 2:
                    result.append(word)

    paginator = Paginator(result, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'all_doc': result,
        'perm': permissions,
        'posts': posts,
        'letters': letters,
        "paginator": paginator
    }
    return render(request, "search_list.html", context)


def reports(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            newrep = form.save(commit=False)
            newrep.author = request.user
            newrep.save()
            messages.success(request, 'Отчёт успешно добавлен.')
            return redirect('reports')
        messages.error(request, 'Что-то пошло не так :(')
        return render(request, 'new_rep.html', context={'form': form})
    form = ReportForm()
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    reports = list(reversed(Report.objects.all()))

    paginator = Paginator(reports, 8)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'reports': reversed(reports), 'form': form,
        'user': request.user, 'perm': permissions, 'posts': posts,
        'paginator': paginator
    }
    return render(request, 'reports.html', context)


def new_rep(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    form = ReportForm(request.POST, request.FILES)

    context = {'form': form, 'perm': permissions}
    return render(request, 'new_rep.html', context)


def report_delete(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if report.author == request.user:
        os.remove(report.file.path)
        report.delete()
        return redirect('reports')
    else:
        return redirect('reports')


def about_developers(request):
    return render(request, 'about_dev.html')
