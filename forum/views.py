from django.shortcuts import render,redirect,get_object_or_404
from forum.models import Topic,Post
from django.views.generic import DetailView,CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import TopicForm,PostForm


def topic_list(request):
    topics = Topic.objects.all().order_by("-created_at")
    return render(request, "Forum/topics_list.html", {"topics": topics})


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'Forum/topics_detail.html'
    context_object_name = 'topic'



class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = 'Forum/topics_create.html' 
    form_class = TopicForm
    success_url = reverse_lazy('forum:topics-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'Forum/posts_create.html' 
    form_class = PostForm
    
