from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    users = models.ManyToManyField(
        "users.User",
        related_name="chatting_rooms",
    )

    def __str__(self) -> str:
        return "Chatting Room."


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="message",
    )

    def __str__(self) -> str:
        return f"{self.user} says {self.text}"


# Create your models here.
