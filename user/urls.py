from django.urls import path

from .views import index, user_login, user_logout, user_signup

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]