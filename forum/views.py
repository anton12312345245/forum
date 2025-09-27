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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] =  self.object.Post.all()
        context['form'] = PostForm()
        return context
    
    def post(self,request,*args,**kwargs):
        Comment_Form = PostForm(request.POST)
        if Comment_Form.is_valid():
            comment = Comment_Form.save(commit=False)
            comment.created_by =  request.user
            comment.topic = self.get_object()
            comment.save()
            return redirect('forum:topics-detail',pk=comment.topic.pk)


class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    template_name = 'Forum/topics_create.html' 
    form_class = TopicForm
    success_url = reverse_lazy('forum:topics-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

