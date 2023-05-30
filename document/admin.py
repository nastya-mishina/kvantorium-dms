from django.contrib import admin
from django.contrib.auth.models import Group

from document.models import Document, Event, Report, SigDoc
from users.models import User

admin.site.site_header = "Администрация"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Admin"


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'middle_name')
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'middle_name', 'position', 'email', 'phone', "password",
                       "is_superuser", 'image'),
            'description': (
                "БАЗОВЫЙ ПАРОЛЬ: 'qwer123ty'. | ЕСЛИ НЕОБХОДИМО СБРОСИТЬ ПАРОЛЬ ДО БАЗОВОГО, ТО НУЖНО В ПОЛЕ 'Пароль' "
                "НУЖНО ВВЕСТИ 'pbkdf2_sha256$390000$jNQoFll3T4NGf109vDxvYX$wzXUUE3zThacoBzb0BE4x89F4N6qtUtpF1z2vYFpg"
                "/c='")
        }),
    )


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('author', "file")


class EventAdmin(admin.ModelAdmin):
    list_display = ('text', "date")


class ReportAdmin(admin.ModelAdmin):
    list_display = ('author', "file")


class SigDocAdmin(admin.ModelAdmin):
    list_display = ('sign_doc', "doc", "signaturer")


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(SigDoc, SigDocAdmin)
