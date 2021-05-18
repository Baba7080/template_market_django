from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.
def devloper_home_view(request):

    return render(request, "devloper/dev_home.html")


class detail_view(DetailView):
    model = template_post
    template_name = 'devloper/detail.html'


