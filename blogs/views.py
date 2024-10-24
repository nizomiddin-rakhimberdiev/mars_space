from django.shortcuts import render, redirect

from users.models import Student
from .forms import CreatePostForm
from .models import BlogPost

# Create your views here.
def blogs_view(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


def create_blog_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            author = Student.objects.get(id=request.user.id)
            BlogPost.objects.create(title=title, image=image, author=author)
            # form.save()  # Save the blog post to the database
            return redirect('blogs_view')
    else:
        form = CreatePostForm()  # Re-render form with errors if not valid
    context = {'form': form}
    return render(request, 'add_blog.html', context=context)