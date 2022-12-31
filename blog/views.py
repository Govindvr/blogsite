from django.shortcuts import render,redirect
from django.db import connection
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# Create your views here.

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def home(request):
    cursor = connection.cursor()
    cursor.execute("SELECT blog_post.id,title,content,date_posted,author_id,username FROM blog_post,auth_user where author_id=auth_user.id order by date_posted desc")
    r = dictfetchall(cursor)
    context = {
        'posts': r
    }
    return render(request,'blog/home.html',context=context)

def blog(request,id):
    cursor = connection.cursor()
    cursor.execute("SELECT blog_post.id,title,content,date_posted,author_id,username FROM blog_post,auth_user where author_id=auth_user.id and blog_post.id={}".format(id))
    post = dictfetchall(cursor)
    post = post[0]
    return render(request,"blog/post.html", context={'post':post})

@login_required(login_url= '/user/login')
def createPost(request):
    print(timezone.now())
    print(request.user.id)
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        query = "INSERT INTO blog_post(title,content,date_posted,author_id) VALUES('{}','{}','{}',{})".format(title,content,timezone.now(),request.user.id)
        cursor = connection.cursor()
        cursor.execute(query)
        return redirect("/")

    return render(request,'blog/create.html')
