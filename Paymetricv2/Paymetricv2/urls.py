from django.contrib import admin
from django.urls import path

from .views import home_page, contact
from accounts.views import RegisterView, login_page
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home_page'),
    path('contact/', contact),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)