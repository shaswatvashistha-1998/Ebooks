from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from firstapp.models import profileinfo
from . import models
from django.http import HttpResponse

# Create your views here.
class Mainpage(ListView):
    template_name='index.html'
    model=models.profileinfo
    context_object_name='books'
class Upload(CreateView):
    template_name='upload.html'
    model=models.profileinfo
    fields=('__all__')
def search(request):
    try:
        q=request.GET.get('q')
    except:
        q=none
    if q:
        q.lower()
        obj=profileinfo.objects.filter(name__icontains=q)
        context={'books':obj}
        template='search.html'
    else:
        template='search.html'
        context={}
    return render(request,template,context)
def genre(request):
    template='index.html'
    return render(request,template)
