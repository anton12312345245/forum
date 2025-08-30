from django.shortcuts import render,redirect,get_object_or_404
from voting.models import Vote, VoteOption, UserVote
from django.views.generic import DetailView,CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from voting.forms import VoteForm

def vote_list(request):
    votes = Vote.objects.all().order_by("-created_at")
    return render(request, "Voting/vote_list.html", {"votes": votes})


class VoteDetailView(DetailView):
    model = Vote
    template_name = 'Voting/vote_detail.html'
    context_object_name = 'vote'



class VoteCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Vote
    template_name = 'Voting/vote_create.html'
    success_url = redirect ('voting:vote-list')
    form_class = VoteForm
    
    def test_func(self):
        return self.request.user.profile.role == 'admin'


class EditYourVoteView(LoginRequiredMixin,View):
    def post(self,request,pk):
        vote = get_object_or_404(Vote,pk=pk)
        option_id = request.POST.get('option')
        option = get_object_or_404(VoteOption,pk=option_id,vote=vote)
        uservote,exists = UserVote.objects.get_or_create(vote=vote,defaults={'option': option},user=request.user)
        if exists == True:
            option.vote_count += 1 
            option.save()
        else:
            if uservote.option != option:
                uservote.option.vote_count -= 1
                uservote.option.save()
                option.vote_count += 1            
                option.save()
                uservote.option = option
                uservote.save() 
        return redirect ('voting:vote-detail',pk=vote.pk)
