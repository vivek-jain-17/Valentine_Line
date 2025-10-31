from django.db import models
import uuid

class Compliment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    share_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text[:50]

class SharedCompliment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    compliment = models.ForeignKey(Compliment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared: {self.compliment.text[:30]}"
