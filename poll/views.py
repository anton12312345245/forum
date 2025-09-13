from django.shortcuts import render,redirect,get_object_or_404
from poll.models import Poll, PollOption, UserPollVote
from django.views.generic import DetailView,CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from poll.forms import PollForm,PollOptionSet

def poll_list(request):
    polls = Poll.objects.all().order_by("-created_at")
    return render(request, "Poll/poll_list.html", {"polls": polls})


class PollDetailView(DetailView):
    model = Poll
    template_name = 'Poll/poll_detail.html'
    context_object_name = 'poll'



class PollCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Poll
    template_name = 'Poll/poll_create.html'
    success_url = reverse_lazy ('poll:poll-list')
    form_class = PollForm
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form_set'] = PollOptionSet(self.request.POST,instance=self.object)
        else:
             context['form_set'] = PollOptionSet(instance=self.object)
        return context     
         
    def form_valid(self,form):
        context = self.get_context_data()
        form_set = context['form_set']
        if form_set.is_valid():
            form.instance.created_by = self.request.user
            self.object = form.save()
            form_set.instance = self.object
            form_set.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def test_func(self):
        return self.request.user.profile.role == 'admin'


class EditYourPollView(LoginRequiredMixin,View):
    def post(self,request,pk):
        poll = get_object_or_404(Poll,pk=pk)
        option_id = request.POST.get('option')
        option = get_object_or_404(PollOption,pk=option_id,poll=poll)
        if UserPollVote.objects.filter(poll=poll,user=request.user).exists():
            return redirect('poll:poll-detail',pk=poll.pk)
        UserPollVote.objects.create(poll=poll,option=option,user=request.user)
        option.poll_count += 1
        option.save()
        return redirect('poll:poll-detail',pk=poll.pk)