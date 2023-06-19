from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import Blogform
from django.urls import reverse
from .models import Blogmodel,Profile,BlogComment
from django.contrib.auth import logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from blogapp.templatetags import extras



def logout_view(request):
    logout(request)
    return redirect("home")

def home(request):
    blogs = Blogmodel.objects.all()
    popular = Blogmodel.objects.order_by('views')[::-1]
    # print(blogs)
    return render (request , 'home.html',{'blogs':blogs,'popular':popular[:3]})
def login(request):
    return render(request , 'login.html')
def viewpage(request,slug):
    commentwalapost = Blogmodel.objects.get ( slug=slug )
    if commentwalapost:
         comment = BlogComment.objects.filter ( post=commentwalapost,parent=None)
         replies = BlogComment.objects.filter(post=commentwalapost).exclude(parent = None)
         print(replies)
         reply_dict={}
         for r in replies:
             if r.parent not  in reply_dict:
                 reply_dict[r.parent] = [r]
             else:
                 reply_dict[r.parent].append(r)
         print("dict",reply_dict)
    msg = False
    post = Blogmodel.objects.filter(slug = slug)[0]
    post.views += 1
    print(post.views)
    post.save()
    user = request.user
    # print("user",user)
    if post.likes.filter ( id=user.id ):
        post.likes.add ( user )
        msg = True
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            print("authenticates",user)
            if post.likes.filter ( id=user.id ):
                post.likes.remove(user)
                msg = False
            else:
                  post.likes.add(user)
                  msg = True



    return render(request,'viewpage.html',{'post':post,'msg':msg,'comment':comment,'reply_dict':reply_dict})
def addblog(request):
    context ={'form':Blogform ,'user':request.user}
    try:
        if request.method == 'POST':
                form = Blogform ( request.POST )
                title = request.POST.get("title")
                image = request.FILES.get("image")
                user = request.user
                if form.is_valid ():
                    content = form.cleaned_data["content"]
                blog = Blogmodel(user = user , title = title , images = image , content = content)
                blog.save()
                return redirect( "/blogs/home/" )
    except Exception as e :
        print(e)
    return render(request,'addblogs.html',context)
def register(request):
    return render(request, "register.html")
def forget(request):
    return render(request, 'forget.html')
def seeblogs(request):
    context ={}
    try:
         blogs = Blogmodel.objects.filter(user = request.user)

         context['blogs'] = blogs
    except Exception as e:
        print(e)
    return render (request, 'seeblog.html',context)
def delete(request,id):
    try:
       d = Blogmodel.objects.get(id = id)
       if d.user == request.user:
             print(d.title,"deleted")
             d.delete()
    except Exception as e:
        print(e)
    return redirect('/blogs/seeblog/')

def update(request,slug):
    context={}
    try:
        blogobj = Blogmodel.objects.get(slug = slug)
        if blogobj.user != request.user:
             return redirect('/seeblog')
        context['user']  = request.user
        context['blogobj'] = blogobj
        intaial_data = {
                  'content': blogobj.content
               }
        form = Blogform(initial = intaial_data)
        context ['form'] =  form
        if request.method == 'POST':
                form = Blogform ( request.POST )
                title = request.POST.get("title")
                image = request.FILES.get("image")
                user = request.user
                if form.is_valid ():
                    content = form.cleaned_data["content"]
                blog = Blogmodel(user = user , title = title , images = image , content = content)
                blog.save()
                return HttpResponse("Suceesfully updated")
    except Exception as e:
        print(e)
    return render (request, 'update.html' ,context)


def verify(request,token):
    try:
        obj  = Profile.objects.get(token = token)
        # print(obj,"profileobj")
        if obj :
            obj.verified = True
            obj.save()
    except Exception as e:
        print(e,"e")
    return HttpResponse("Verified")

def search(request):
   returnblogs = []
   shyd=[]
   blogs = request.POST.get('searchbtn')
   search = Blogmodel.objects.all()
   returnblogs = search
   for i in search:
       # print(i.user)
       if blogs in i.title.lower() or blogs in i.content.lower() :
           print(i)
           shyd.append(i)
   if len(shyd) > 0:
       returnblogs  = shyd
   # print('retrun',returnblogs)
   return render(request,'search.html',{'list':returnblogs})

def comment(request,slug):
    if request.method == 'POST':
               comment = request.POST.get('comment')
               user = request.user
               print("reply",comment)
               parent = request.POST.get ('parent')
               post = Blogmodel.objects.get(slug= slug)
               if parent == None:
                    p = BlogComment(user=user,comment=comment,post=post,parent=None)
                    # p.save ()
               else:
                   parent = BlogComment.objects.get(id = parent)
                   p = BlogComment ( user=user, comment=comment, post=post,parent=parent )
               p.save()
               messages.success(request, "Comment has been successfully done" )

    return redirect(f'/blogs/viewpage/{slug}/')
