from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import (
    Post,
    Like,
    Comment,
    Follow,
    Profile,
    Notification
)


def home(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'social/home.html', {
        'posts': posts
    })


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'social/register.html',
                {'error': 'Username already exists.'}
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Profile.objects.create(user=user)

        login(request, user)

        return redirect('home')

    return render(request, 'social/register.html')


def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(
            request,
            'social/login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'social/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_post(request):

    if request.method == 'POST':

        content = request.POST['content']
        image = request.FILES.get('image')

        Post.objects.create(
            user=request.user,
            content=content,
            image=image
        )

        return redirect('home')

    return render(request, 'social/create_post.html')


@login_required
def like_post(request, id):

    post = get_object_or_404(Post, id=id)

    like = Like.objects.filter(
        user=request.user,
        post=post
    )

    if like.exists():

        like.delete()

    else:

        Like.objects.create(
            user=request.user,
            post=post
        )

        if post.user != request.user:

            Notification.objects.create(
                recipient=post.user,
                sender=request.user,
                message=f"{request.user.username} liked your post",
                post=post
            )

    return redirect('home')


@login_required
def comment_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':

        text = request.POST['text']

        Comment.objects.create(
            user=request.user,
            post=post,
            text=text
        )

        if post.user != request.user:

            Notification.objects.create(
                recipient=post.user,
                sender=request.user,
                message=f"{request.user.username} commented on your post",
                post=post
            )

    return redirect('home')


def profile(request, username):

    profile_user = get_object_or_404(
        User,
        username=username
    )

    posts = Post.objects.filter(
        user=profile_user
    ).order_by('-created_at')

    followers = Follow.objects.filter(
        following=profile_user
    ).count()

    following = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = False

    if request.user.is_authenticated:

        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(
        request,
        'social/profile.html',
        {
            'profile_user': profile_user,
            'posts': posts,
            'followers': followers,
            'following': following,
            'is_following': is_following
        }
    )


@login_required
def follow_user(request, username):

    user_to_follow = get_object_or_404(
        User,
        username=username
    )

    if request.user != user_to_follow:

        follow = Follow.objects.filter(
            follower=request.user,
            following=user_to_follow
        )

        if follow.exists():

            follow.delete()

        else:

            Follow.objects.create(
                follower=request.user,
                following=user_to_follow
            )

            Notification.objects.create(
                recipient=user_to_follow,
                sender=request.user,
                message=f"{request.user.username} started following you"
            )

    return redirect(
        'profile',
        username=username
    )


def explore(request):

    users = User.objects.all().order_by('username')

    posts = Post.objects.all().order_by('-created_at')

    return render(
        request,
        'social/explore.html',
        {
            'users': users,
            'posts': posts
        }
    )


def search_users(request):

    query = request.GET.get('q', '')

    users = User.objects.filter(
        username__icontains=query
    )

    return render(
        request,
        'social/search.html',
        {
            'users': users,
            'query': query
        }
    )


@login_required
def notifications(request):

    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by('-created_at')

    Notification.objects.filter(
        recipient=request.user,
        is_read=False
    ).update(is_read=True)

    return render(
        request,
        'social/notifications.html',
        {
            'notifications': notifications
        }
    )