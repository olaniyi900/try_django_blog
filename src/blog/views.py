from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from .forms import BlogPostModelForm

# Create your views here.
def blog_list(request):
    obj = BlogPost.objects.all()
    template_name = 'blog/blog_list.html'
    context = {'posts':obj}
    return render(request, template_name, context)

def blog_create(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        # print(form.cleaned_data)
        # obj = BlogPost.objects.create(**form.cleaned_data)
        form =  BlogPostModelForm()
    template_name = 'blog/blog_create.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_detail(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog/blog_detail.html'
    context = {'blog':obj}
    return render(request, template_name, context)

def blog_delete(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    template_name = 'blog/blog_delete.html'
    context = {'object':obj}
    return render(request, template_name, context)


def blog_update(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = BlogPostModelForm()
    template_name = 'blog/blog_update.html'
    context = {'form':form}
    return render(request, template_name, context)
