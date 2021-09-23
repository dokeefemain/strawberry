
# HttpResponse is used to
# pass the information
# back to view
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Users, Posts, Comments, Communities
from django.views.generic.list import ListView
import pandas as pd
from django_pandas.io import read_frame
# Defining a function which
# will receive request and
# perform task depending
# upon function definition


class create_account(CreateView):
    #model = Post
    model = Users
    fields = ['UserName','Password']
    template_name = 'C:/Python/strawberry/strawberry/templates/strawberry/create_user.html'
    success_url = ''

    def save(self):
        obj = super(create_account, self).save(commit=False)
        query_results = Users.objects.all()
        df = read_frame(query_results.values())
        max_id = df['UserID'].max()+1
        obj.UserID = max_id
        obj.save()
        return obj

class create_post(CreateView):
    #model = Post
    model = Posts
    fields = ['Community','Title','Post']
    template_name = 'C:/Python/strawberry/strawberry/templates/strawberry/create_post.html'
    success_url = ''