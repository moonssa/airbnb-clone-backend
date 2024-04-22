from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experience.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    rating = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"
