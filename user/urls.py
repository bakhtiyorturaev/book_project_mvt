from django.urls import path
from .models import CustomerUser
from .views import index, user_login, user_logout, user_signup

urlpatterns = [
    path('', user_login, name='login'),
    path('', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),
]

