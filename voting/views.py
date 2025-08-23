from django.shortcuts import render
from voting.models import Vote, VoteOption, UserVote
from django.views.generic import DetailView,CreateView,View

def vote_list(request):
    votes = Vote.objects.all().order_by("-created_at")
    return render(request, "Voting/vote_list.html", {"votes": votes})


class VoteDetailView(DetailView):
    model = Vote
    template_name = 'Voting/vote_detail.html'
    context_object_name = 'vote'



class VoteCreateView(CreateView):
    pass


class EditYourVoteView(View):
    pass


