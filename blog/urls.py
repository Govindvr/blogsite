from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog-home'),
    path('profile/',views.userProfile, name = 'blog-profile'),
    path('blog/<int:id>',views.viewBlog, name = 'blog-details'),
    path('addPost',views.createPost, name = 'blog-create'),
    path('blog/addComment/<int:id>',views.addComment, name = 'add-comment'),


]