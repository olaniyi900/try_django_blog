from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_list(request):
    obj = BlogPost.objects.all()
    template_name = 'blog_list.html'
    context = {'posts':obj}
    return render(request, template_name, context)
