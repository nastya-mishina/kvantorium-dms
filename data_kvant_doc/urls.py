from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from users.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('users.urls'), name='user_profile'),
    path('login/', views.LoginView.as_view(
        template_name='registration/login.html',
        authentication_form=UserLoginForm
    ),
         name='user_login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('document.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
