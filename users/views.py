from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UserRegisterForm



def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response(
                'create_success.html',)
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
        'output' : ''
        }

    return HttpResponse(template.render(context,request))