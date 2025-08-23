from django.db import models

from django.contrib.auth.models import User


class Vote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_votes")

    def __str__(self):
        return self.title


class VoteOption(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    vote_count = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.text} ({self.vote.title})"


class UserVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="user_votes")
    option = models.ForeignKey(VoteOption, on_delete=models.CASCADE, related_name="user_votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    voted_at = models.DateTimeField(auto_now=True)



