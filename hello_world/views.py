from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "hello_world/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`hello_world.Post`.

    **Context**

    ``post``
        An instance of :model:`hello_world.Post`.

    **Template:**

    :template:`hello_world/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    return render(
    request,
    "hello_world/post_detail.html",
    {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
         "comment_form": comment_form,
    },
    )