from django.urls import path
from announcment import views

app_name = 'announcment'

urlpatterns = [
    path("", views.announcment_list, name="announcment-list"),
    path("detail/<int:pk>",views.AnnouncmentDetailView.as_view(), name="announcment-detail"),
    path('create/',views.CreateAnnouncmentView.as_view(), name="announcment-create"),
    path('delete/<int:pk>',views.DeleteAnnouncmentView.as_view(), name="announcment-delete")
]
