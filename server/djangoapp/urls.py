# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import get_cars

app_name = 'djangoapp'
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('register', views.registration, name='register'),
    path('get_cars', views.get_cars, name='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
