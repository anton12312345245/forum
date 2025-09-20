from django.shortcuts import render,redirect,get_object_or_404
from announcment.models import Announcment
from django.views.generic import DetailView,CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy


def announcment_list(request):
    announcment = Announcment.objects.all().order_by("-created_at")
    return render(request, "Announcment/announcment_list.html", {"announcment": announcment})


class AnnoucmentDetailView(DetailView):
    model = Announcment
    template_name = 'Announcment/announcment_detail.html'
    context_object_name = 'announcment'

