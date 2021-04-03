from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView

urlpatterns = [

    path('', HomeView.as_view(), name ="home"),
    path('PostDetail/<int:pk>', PostDetailView.as_view(), name ="post-detail"),
    path('add_post/', AddPostView.as_view(), name= "add_post"),
    path('PostDetail/edit/<int:pk>', UpdatePostView.as_view(), name= "update_post"),
    path('DeleteDetail/<int:pk>/delete', DeletePostView.as_view(), name= "delete_post"),
    path('like/<int:pk>', LikeView, name = 'like_post')
]

