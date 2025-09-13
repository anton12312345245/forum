from django.db import models

from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_polls")

    def __str__(self):
        return self.title
    

class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    poll_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} ({self.poll.title})"
    

class UserPollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="user_poll")
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE, related_name="user_poll")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="polls")
    voted_at = models.DateTimeField(auto_now=True)