from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
        path('',views.indexView,name="home"),
        path('dashboard/',views.dashboardView,name="dashboard"),
        path('login/',LoginView.as_view(next_page='blog-home'),name="login_url"),
        path('register/',views.registerView,name="register_url"),
        path('logout/',LogoutView.as_view(next_page='blog-home'),name="logout"),
        path('profile/',views.profileView,name="profile"),
        path('data/',views.dataView,name="data"),
        path('update/',views.updateView,name="update"),
]
