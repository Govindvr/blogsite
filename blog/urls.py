from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog-home'),
    path('createpost/',views.createPost, name = 'blog-create'),
    path('blog/<int:id>',views.viewBlog, name = 'blog-details'),
    path('blog/addComment/<int:id>',views.addComment, name = 'add-comment'),


]