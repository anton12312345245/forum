from django.urls import path
from forum import views

app_name = 'forum'

urlpatterns = [
    path("", views.topic_list, name="topics-list"),
    path("topics/<int:pk>/", views.TopicDetailView.as_view(), name="topics-detail"),
    path("topics/create/", views.TopicCreateView.as_view(), name="topics-create"),
    
]
