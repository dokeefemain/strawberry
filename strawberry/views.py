
# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Users, Posts
from django.views.generic.list import ListView
# Defining a function which
# will receive request and
# perform task depending
# upon function definition


class create_account(CreateView):
    #model = Post
    model = Users
    fields = '__all__'
    template_name = 'C:/Python/strawberry/strawberry/templates/strawberry/create_user.html'
    success_url = ''

class create_post(CreateView):
    #model = Post
    model = Posts
    fields = ['title','post']
    template_name = 'C:/Python/strawberry/strawberry/templates/strawberry/post_form.html'
    success_url = ''