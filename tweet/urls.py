from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('tweet/delete/<int:id>',views.delete_tweet, name='delete-tweet'),
    path('tweet/tweet_detail/<int:id>',views.tweet_detail, name='tweet-detail'),
    path('tweet/tweet_detail/delete/<int:id>',views.delete_comment, name='delete-comment'),
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]