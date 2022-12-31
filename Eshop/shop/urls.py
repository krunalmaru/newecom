from django.urls import path
from .views import home,login,signup,cart
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home.MyHome.as_view(), name='home'),
    # path('signup', views.signup,name='signup'),
    path('signup', signup.Signup.as_view(), name='signup'),
    # path('login', views.loginuser, name='login'),
    path('login',login.Login.as_view(), name='login'),
    path('logout',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
