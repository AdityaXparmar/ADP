from django.db import models
from django.conf import settings   

class Note(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title