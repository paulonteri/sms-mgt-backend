from django.urls import path, include
from knox import views as knox_views

from .api import RegisterAPI, LoginAPI, UserAPI, UserInformationAPI, AllUserInformationAPI, GroupAPI

urlpatterns = [
    path('user', UserAPI.as_view()),
    #
    path('userinfo/user', UserInformationAPI.as_view()),
    path('userinfo/all', AllUserInformationAPI.as_view()),
    #
    path('register', RegisterAPI.as_view()),
    #
    path('login', LoginAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logout'),
    #
    path('roles/groups', GroupAPI.as_view()),
    #
    path('', include('knox.urls')),
]
