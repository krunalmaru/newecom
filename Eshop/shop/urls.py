from django.urls import path
from .views import home,login,signup
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home.home, name='home'),
    # path('signup', views.signup,name='signup'),
    path('signup', signup.Signup.as_view(), name='signup'),
    # path('login', views.loginuser, name='login'),
    path('login',login.Login.as_view(), name='login'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
