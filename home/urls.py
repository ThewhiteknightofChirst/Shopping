from .models import Profile
from django.urls import path
from . import views as home
from monan import views as monan
from giohang import views as giohang
from rent import views as rent
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views as user_views
urlpatterns = [
    path('',home.index),
    path('register/', home.register, name='register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('monan/', monan.PostListView.as_view(), name='monan'),
    path('giohang/', giohang.index, name='giohang'),
    path('rent/', rent.show, name='rent'),
    path('rent/emp/', rent.emp, name='rentad'),
    path('profile/', user_views.profile, name= 'profile'),
    path('updatep/', user_views.profileupdate, name = 'updatep')
]
