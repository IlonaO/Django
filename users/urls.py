from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = patterns('',
                       url(r'^login/$', auth_views.login,
                           {'template_name': 'login.html'}, name='login'),
                       url(r'^reset_pass/$', views.reset_pass, name='reset_pass'),
                       url(r'^create/$', views.create_user,
                           name='create_user'),
                       url(r'^create/create_success/$', views.create_success,
                           name='create_success'),
                       url(r'^logout/$', auth_views.logout,
                           {'next_page': '/'}, name='logout'),
                       url(r'^password/reset$',
                           auth_views.password_reset,
                           {'template_name': 'form.html',
                               'post_reset_redirect': 'reset_pass'},
                           name='password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
                           r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                           auth_views.password_reset_confirm,
                           {'template_name': 'password_reset_confirm.html'},
                           name='password_reset_confirm'),
                       url(r'^password/reset/complete$',
                           auth_views.password_reset_complete,
                           {'template_name': 'password_reset_complete.html'},
                           name='password_reset_complete'),
                       url(r'^my_account/$', views.my_account, name='my_account'),
                       )