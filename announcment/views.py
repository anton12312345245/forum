from django.shortcuts import render,redirect,get_object_or_404
from announcment.models import Announcment
from django.views.generic import DetailView,CreateView,View,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .form import AnnouncmentForm 

def announcment_list(request):
    announcment = Announcment.objects.all().order_by("-created_at")
    return render(request, "Announcment/announcment_list.html", {"announcment": announcment})


class AnnouncmentDetailView(DetailView):
    model = Announcment
    template_name = 'Announcment/announcment_detail.html'
    context_object_name = 'announcment'



class CreateAnnouncmentView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Announcment
    template_name = 'Announcment/announcment_create.html'
    success_url = reverse_lazy('announcment:announcment-list')
    form_class = AnnouncmentForm

    def test_func(self):
        return self.request.user.profile.role == 'admin'
        
    def form_valid(self, form):

        form.instance.created_by = self.request.user

        return super().form_valid(form)




class DeleteAnnouncmentView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Announcment
    template_name = 'Announcment/announcment_delete.html'
    success_url = reverse_lazy('announcment:announcment-list')
    def test_func(self):
        return self.request.user.profile.role == 'admin'
    
