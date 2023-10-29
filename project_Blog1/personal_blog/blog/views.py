from django.shortcuts import render,HttpResponseRedirect
from .models import Post,Comment,Category
from .forms import CommentForm,PostForm

def blog_index(request):
    posts=Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
    }
    return render(request,"blog/index.html",context)

def blog_category(request,category):
    posts=Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context={
        "posts":posts,
        "category":category,
    }
    return render(request,"blog/category.html",context)

def blog_detail(request,pk):
    post=Post.objects.get(pk=pk)
    
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    comments=Comment.objects.filter(post=post)
    context={
        "post":post,
        "comments":comments,
        "form":form,
    }
    return render(request,"blog/detail.html",context)

def create_post(request):
    category1=Category.objects.get(pk=2)
    form=PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=Post(
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
            )
            post.save()
            post.categories.add(category1)
            return HttpResponseRedirect(request.path_info)
    context={
        "form":form,
        "categories":category1,
    }
    return render(request,'blog/create_post.html',context)
    