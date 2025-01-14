from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report on {self.listing.title} by {self.reporter}"
