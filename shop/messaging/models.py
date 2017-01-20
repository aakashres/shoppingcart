from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Message(Timestampable):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="sent_messages",
        null=True, blank=True,
        verbose_name="sender"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="received_messages",
        null=True, blank=True,
        verbose_name="recipient"
    )
    body = models.TextField("Message Body", blank=True)

    def __str__(self):
        return self.sender + "->" + self.recipient

    class Meta:
        ordering = ["-updated_at", "-id"]
