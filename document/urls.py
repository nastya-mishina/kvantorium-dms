from django.urls import path

from . import views
from .views import doc_list

urlpatterns = [
    path(
        'delete_doc/<int:document_id>/',
        views.document_delete,
        name='document_delete'
    ),
    path(
        'check_sig/<int:document_id>/',
        views.check_sig,
        name='check_sig'
    ),
    path(
        'sig_doc/<int:document_id>/',
        views.signature,
        name='signature'
    ),

    path(
        'delete_event/<int:event_id>/',
        views.event_delete,
        name='event_delete'
    ),
    path(
        'delete_report/<int:report_id>/',
        views.report_delete,
        name='report_delete'
    ),
    path('my_doc/', views.my_doc, name='my_doc'),
    path('reports/', views.reports, name='reports'),
    path('new_report/', views.new_rep, name='new_report'),
    path('events/', views.events, name='events'),
    path('new_event/', views.new_event, name='new_event'),
    path('new_doc/', views.new_doc, name='new_doc'),
    path('notifications/', views.notifications, name='notifications'),
    path('event/<int:event_id>/',
         views.event_one,
         name='event_one'
         ),
    path('search/', views.search_list, name='search_list'),
    path('about-dev/', views.about_developers, name='about_dev'),
    path('', doc_list, name='doc_list'),

]
