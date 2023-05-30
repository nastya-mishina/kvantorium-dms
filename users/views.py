from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from document.models import Document

from .forms import (ChangePasswordForm, SignatureForm,
                    User)


@login_required
def profile(request, username):
    count = 0
    user = request.user
    author = get_object_or_404(User, username=username)
    documents = []
    for document in Document.objects.all():
        if document.author == author:
            documents.append(document)
    for doc in documents:
        if doc.author == author:
            count += 1
    if author.is_superuser:
        au_permissions = 1
    else:
        au_permissions = 0

    if user.is_superuser:
        permissions = 1
    else:
        permissions = 0

    paginator = Paginator(documents, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "profile.html", {
        "author": author, "count": count, "documents": documents, 'au_perm': au_permissions, 'perm': permissions,
        'posts': posts, 'paginator': paginator}, )


def all_users(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    all_users = User.objects.all()

    paginator = Paginator(all_users, 9)
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
        "all_users": all_users,
        "username": User.username,
        'perm': permissions,
        'posts': posts,
        'paginator': paginator
    }
    return render(request, 'personal.html', context)


def settings(request):
    if request.user.is_superuser:
        permissions = 1
    else:
        permissions = 0
    u = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = request.POST.get("old_password")
            new_pass = request.POST.get("new_pass")
            new_pass_rep = request.POST.get("new_pass_rep")
            if check_password(old_password, u.password):
                if new_pass == new_pass_rep:
                    u.set_password(new_pass)
                    u.save()
                    messages.success(request, 'Пароль успешно изменён')
                    return redirect('login')
                else:
                    messages.error(request, 'Новые пароли не совпадают')
                    return render(request, 'settings.html', context={'form': form, 'perm': permissions})
            else:
                messages.error(request, 'Старый пароль не совпадает')
                return render(request, 'settings.html', context={'form': form, 'perm': permissions})
    else:
        form = ChangePasswordForm()

    if request.method == 'POST':
        form2 = SignatureForm(request.POST, request.FILES)
        if form2.is_valid():
            u.PublicKey = request.FILES.get("PublicKey")
            u.save()
            messages.success(request, 'Ключ успешно добавлен')
            return redirect('settings')
        messages.error(request, '*ОШИБКА*')
        return render(request, 'settings.html', context={'form': form, 'perm': permissions})
    else:
        form2 = SignatureForm()

    context = {
        "username": User.username,
        'perm': permissions,
        'form': form,
        'form2': form2,
        'user': u
    }
    return render(request, 'settings.html', context)
