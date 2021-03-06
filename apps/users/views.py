from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader

from apps.blog.models import Post, Comment
from .forms import UserRegisterForm


def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response(
                'create_success.html', )
    else:
        form = UserRegisterForm()
    return render(request, 'create_user.html', {
        'form': form,
    })


def create_success(request):
    return render_to_response(
        'create_success.html',
    )


def reset_pass(request):
    template = loader.get_template("reset_pass.html")
    context = {
        'output': ''
    }

    return HttpResponse(template.render(context, request))


def my_account(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user)
    logged_in_user_comments = Comment.objects.filter(author=logged_in_user)

    return render(request, 'my_account.html', {
        'posts': logged_in_user_posts, 'comments': logged_in_user_comments})
