from django.shortcuts import render
from voting.models import Vote, VoteOption, UserVote

def vote_list(request):
    votes = Vote.objects.all().order_by("-created_at")
    return render(request, "voting/vote_list.html", {"votes": votes})


def vote_detail(request):
    pass


def vote_create(request):
    pass


def cast_vote(request):
    pass


