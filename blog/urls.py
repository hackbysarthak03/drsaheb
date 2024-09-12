from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Blogs, name='blogs'),
    path('write/', views.writeBlog),
    path('manage/', views.myBlogs),
    path('delete/<int:id>', views.deleteBlog),
    path('update/<int:id>', views.updateBlog)
]