from django.core.paginator import Paginator
from .models import Post


def paginatePosts(page_number, user_id, filters={}):

    posts = Post.objects.filter(**filters)
    paginator = Paginator(posts, 10)
    page = paginator.get_page(page_number)
    posts = page.object_list
    for post in posts:
        post.has_liked = post.likers.filter(pk=user_id).exists()
        post.likers_count = post.likers.count()

    has_next = page.has_next
    has_previous = page.has_previous
    return posts, has_next, has_previous
