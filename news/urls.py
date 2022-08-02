from django.urls import path
from . import views
from accounts.views import login_view, logout_view, SignUp, register_view


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login_view, name='login_view'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('SignUp/', SignUp, name='SignUp'),
    path('logout/', login_view, name='logout_view'),
    path('register/', register_view, name='register_view')
    # path('forms', forms, name='forms')
]
