from django.urls import path
from .models import CustomerUser
from .views import (index, user_login, logout_user, user_signup, ProfileUpdateView, profile_view
                    )

app_name = 'user'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', user_signup, name='signup', ),
    # path('password-res-con/', name='password-reset-confirm'),
    path('profile/', profile_view, name='profile'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),

]
