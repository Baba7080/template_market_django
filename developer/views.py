from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
from .forms import *
# Create your views here.
def devloper_home_view(request):

    return render(request, "devloper/dev_home.html")


class detail_view(DetailView):
    model = template_post
    template_name = 'devloper/detail.html'


def registration(request):
    d_form = CustomerRegistrationForm(request.POST)

    if request.method == 'POST':
        d_form = CustomerRegistrationForm(request.POST)
        if d_form.is_valid():
            d_fom.save()
            return HttpResponse('login')

    else:
        form = CustomerRegistrationForm()

    return render(request, 'devloper/developer_registration.html', {'d_form': d_form})
