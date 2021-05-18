from django.shortcuts import render
from developer.models import template_post
from django.views.generic import DetailView

# Create your views here.
def home_view(request):
    templa = template_post.objects.all()
    return render(request, "home.html",{'templa':templa})
def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/template_post")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response

	raise Http404
# def detail_view(request,DetailView):

class detail_view(DetailView):
    model = template_post
    template_name = 'devloper/detail.html'