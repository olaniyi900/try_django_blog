from django.shortcuts import render
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def blog_list(request):
    obj = BlogPost.objects.all()
    template_name = 'blog/blog_list.html'
    context = {'posts':obj}
    return render(request, template_name, context)

def blog_create(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template_name = 'blog/blog_create.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_detail(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog/blog_detail.html'
    context = {'blog':obj}
    return render(request, template_name, context)

def blog_delete(request):
    template_name = 'blog/blog_delete.html'
    context = {'form':'ade'}
    return render(request, template_name, context)


def blog_update(request):
    template_name = 'blog/blog_update.html'
    context = {'form':'ade'}
    return render(request, template_name, context)
