from django.db import models


class Forum(models.Model):
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="comments")
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name="children")

    text = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.text
