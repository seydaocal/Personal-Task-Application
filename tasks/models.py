from django.db import models
from django.conf import settings
from django.db.models import F


class Category(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Kategoriler"

class Task(models.Model):
    status_choices = [
        ("done", "Tamamlandı"),
        ("continuous","Devam ediyor.."),
        ("waiting", "Beklemede"),
        ("canceled", "İptal edildi")
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_urgent = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=status_choices,default="continuous")
    
    class Meta:
        ordering = ["-is_urgent", F("due_date").asc(nulls_last=True)]
        verbose_name_plural = "Görevler"

    def __str__(self):
        return self.title 


