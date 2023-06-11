import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .helpers import paginatePosts
from .forms import PostForm
from .models import User, Post


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
        return HttpResponseRedirect(reverse('index'))
    form = PostForm()

    page_number = request.GET.get('page', 1)
    posts, has_next, has_previous = paginatePosts(page_number, request.user.id)

    return render(request, "network/index.html", {'form': form, 'posts': posts, 'has_next': has_next, 'has_previous': has_previous, 'page_number': page_number})


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    amIFollowing = request.user.following.filter(
        id=user.id).exists() if request.user.is_authenticated else False
    if request.method == 'POST' and request.user.is_authenticated and user.id != request.user.id:
        if amIFollowing:
            request.user.following.remove(user)
        else:
            request.user.following.add(user)
        amIFollowing = not amIFollowing

    user_id = user.id
    username = user.username

    followers = user.user_followers.count()
    following = user.following.count()
    page_number = request.GET.get('page', 1)
    posts, has_next, has_previous = paginatePosts(
        page_number, request.user.id, {'created_by': user_id})

    return render(request, "network/profile.html", {'user_id': user.id, 'username': username, 'posts': posts, 'followers': followers, 'following': following,
                                                    'amIFollowing': amIFollowing, 'page_number': page_number, 'has_next': has_next, 'has_previous': has_previous})


@login_required
def following(request):
    user_following = request.user.following.all()
    page_number = request.GET.get('page', 1)
    posts, has_next, has_previous = paginatePosts(
        page_number, request.user.id, {'created_by__in': user_following})

    return render(request, 'network/following.html', {'posts': posts, 'page_number': page_number, 'has_next': has_next, 'has_previous': has_previous})


@login_required
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    # EDIT POST (text, like, etc...)
    if post is not None and request.method == 'PATCH':
        body = json.loads(request.body)

        if body.get('toogle_like'):
            if post.likers.filter(pk=request.user.id).exists():
                liked = False
                post.likers.remove(request.user)
            else:
                liked = True
                post.likers.add(request.user)
            return JsonResponse({'liked': liked, 'likers': post.likers.count()})
        if post.created_by.id != request.user.id:
            return JsonResponse({'error': "You don't have permission to do that.", 'updated_text': post.text}, status=403)

        form = PostForm({'text': body.get('text')}, instance=post)

        if form.is_valid():
            post = form.save()
            return JsonResponse({'updated_text': post.text})
        return JsonResponse({'error': "Invalid request payload", 'updated_text': post.text}, status=400)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
