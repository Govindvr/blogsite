from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'blog-home'),
    path('createpost/',views.createPost, name = 'blog-create'),

]