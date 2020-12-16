from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from category.models import Category
from lib.functions import get_category
from post.models import Post


def post_list(request):
    posts = Post.objects.all()
    title = posts.values_list('title', flat=True)
    return HttpResponse("post-page count: {} <br> titles :{}".format(posts.count(), ' '.join(title)))


def home(request):
    post_count = Post.objects.all().count()
    post_list=Post.objects.all()[2:post_count]


    user=request.user.id
    category_list=Category.objects.all()

    context={'post_count':post_count,
             "post_titles":post_list,"category_list":category_list}

    return render(request,"weblog/home.html",context)


def post_details(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={"post":post,"category_list":get_category()}
    return render(request,'weblog/postSingle.html',context=context)


def get_post_username(request,id):

    post_user=Post.objects.filter(author__id=id)
    context = {"post_user": post_user, "category_list": get_category()}

    return render(request, 'weblog/userpost.html', context=context)

def get_post_category(request,id):

    post_cat=Post.objects.filter(category__id=id)
    context = {"post_cat": post_cat, "category_list": get_category()}

    return render(request, 'weblog/categorypost.html', context=context)