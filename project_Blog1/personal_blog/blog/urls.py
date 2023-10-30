from django.urls import path
from . import views

urlpatterns=[
    path('', views.blog_index ,name='blog-index'),
    path('category/<category>', views.blog_category, name='blog-category'),
    path('post/<int:pk>/',views.blog_detail, name="blog-detail"),
    path('post/',views.create_post,name="blog-post"),
    path('post/<int:post_id>/delete/',views.blog_delete,name="post-delete")
]