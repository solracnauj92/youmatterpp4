from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

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

    return render(
        request,
        "hello_world/post_detail.html",
        {"post": post,
        "coder": "Juan Carlos Diaz Lara"},
    )