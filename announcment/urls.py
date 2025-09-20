from django.urls import path
from announcment import views

app_name = 'announcment'

urlpatterns = [
    path("", views.announcment_list, name="announcment-list"),
    path("detail/<int:pk>", views.AnnoucmentDetailView.as_view(), name="announcment-detail")
]
