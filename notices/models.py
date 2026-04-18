from django.db import models

from django.contrib.auth.models import User

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('academic', 'Academic'),
        ('event', 'Event'),
        ('urgent', 'Urgent'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='general'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
# Create your models here.
