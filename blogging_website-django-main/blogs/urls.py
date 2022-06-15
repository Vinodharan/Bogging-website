from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:post_id>/', views.post_details, name='post_details'),
    path('search/', views.search, name='search'),
    path('myblogs/', views.myblogs, name='myblogs'),
    path('addblog/', views.addBlog, name='addblog'),
    path('update/<int:post_id>/', views.updateBlog, name='updateBlog'),
    path('delete/<int:post_id>/', views.deleteBlog, name='deleteBlog'),
]