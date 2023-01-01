from django.shortcuts import render,redirect
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect


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

def viewBlog(request,id):
    cursor = connection.cursor()
    cursor.execute("SELECT blog_post.id,title,content,date_posted,author_id,username FROM blog_post,auth_user where author_id=auth_user.id and blog_post.id={}".format(id))
    post = dictfetchall(cursor)
    post = post[0]
    
    cursor = connection.cursor()
    cursor.execute("SELECT blog_comment.id,content,date_posted,author_id,post_id,username FROM blog_comment,auth_user where author_id=auth_user.id and post_id={} order by date_posted desc".format(id))
    comments = dictfetchall(cursor)
    context={
        'post': post,
        'comments': comments
    }
    print(post)
    return render(request,"blog/post.html", context=context)

@login_required(login_url= '/user/login')
def addComment(request,id):
    if request.method=='POST':
        data = request.POST['comment']
        user = request.user.id
        cursor = connection.cursor()
        cursor.execute("INSERT INTO blog_comment(author_id,post_id,content,date_posted) VALUES({},{},'{}','{}')".format(user,id,data,timezone.now()))

    return HttpResponseRedirect(reverse("blog-details", kwargs={"id":id}))

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
