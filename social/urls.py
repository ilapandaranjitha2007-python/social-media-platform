from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'explore/',
        views.explore,
        name='explore'
    ),

    path(
        'search/',
        views.search_users,
        name='search_users'
    ),

    path(
        'notifications/',
        views.notifications,
        name='notifications'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'post/create/',
        views.create_post,
        name='create_post'
    ),

    path(
        'post/<int:id>/like/',
        views.like_post,
        name='like_post'
    ),

    path(
        'post/<int:id>/comment/',
        views.comment_post,
        name='comment_post'
    ),

    path(
        'profile/<str:username>/',
        views.profile,
        name='profile'
    ),

    path(
        'profile/<str:username>/follow/',
        views.follow_user,
        name='follow_user'
    ),
]