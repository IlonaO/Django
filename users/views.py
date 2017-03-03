from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response


class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = 'create_success'
    template_name = 'form.html'

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