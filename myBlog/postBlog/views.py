from django.shortcuts import render
from .models import postBlog
from .forms import postForm,UserRegistrationFrom
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')


def post_list(request):
    posts=postBlog.objects.all().order_by('-created_at')
    return render(request,'post_list.html',{'posts':posts})

@login_required
def post_create(request):
    if request.method=="POST":
      form=postForm(request.POST,request.FILES)
      if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('post_list')

            

    else:
        form=postForm()
    return render(request,'post_form.html',{'form':form})

@login_required
def post_edit(request,post_id):
    post=get_object_or_404(postBlog,pk=post_id,user=request.user)
    if request.method=='POST':
        form=postForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('post_list')
    else:
        form=postForm(instance=post)
    return render(request,'post_form.html',{'form':form})


@login_required
def post_delete(request,post_id):
    post=get_object_or_404(postBlog,pk=post_id,user=request.user)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request,'post_confirm_delete.html',{'post':post})
    
    
def register(request):
    if request.method=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
                user=form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request,user)
                return redirect('post_list')
     
    else:
        form=UserRegistrationFrom()
        
    return render(request,'registration/register.html',{'form':form})
