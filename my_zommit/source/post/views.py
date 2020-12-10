from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from category.models import Category
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    title = posts.values_list('title', flat=True)
    return HttpResponse("post-page count: {} <br> titles :{}".format(posts.count(), ' '.join(title)))


def home(request):
    post_list=Post.objects.all()
    # post_titles=post_list.values_list('title',flat=True)

    user=request.user.id
    category_list=Category.objects.all()

    post_count = Post.objects.filter(author=user).count()
    context={'first_name': 'John', 'last_name': 'Doe','post_count':post_count,
             "post_titles":post_list,"category_list":category_list}
    print(category_list)
    return render(request,"weblog/home.html",context)


def post_details(request,pk):
    post=Post.objects.filter(pk=pk).first()
    context={"post":post}
    return render(request,'weblog/detail.html',context=context)
