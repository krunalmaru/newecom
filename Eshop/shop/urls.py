from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup,name='signup'),
    path('login', views.loginuser, name='login'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
