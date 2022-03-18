from django.shortcuts import get_object_or_404, render

from .models import Blog, Comment, Socials
from .forms import CommentForm


def index(request):
    obj = Blog.objects.all()
    socls = Socials.objects.all()
    return render(request, 'blog.html', {'obj': obj, 'socls': socls})


def single_blog(request, slug):
    obj = get_object_or_404(Blog, slug=slug)
    socls = Socials.objects.all()
    comments = obj.comments.filter(accepted=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # create comment but do not save to datebase
            new_comment = comment_form.save(commit=False)
            # assign the current blog to the comment
            new_comment.post = obj
            # save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'object':obj, 'socls': socls, 'comments': comments, 'comment_form':comment_form, 'new_comment':new_comment}
    return render(request, 'single-blog.html', context=context)
