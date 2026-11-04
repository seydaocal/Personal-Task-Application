from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "category", "due_date", "due_time", "status", "is_urgent"]
        labels = {
            "title": "Başlık",
            "description": "Açıklama",
            "category": "Kategori",
            "due_date": "Son tarih",
            "due_time": "Saat",
            "status": "Durum",
            "is_urgent": "Acil ★",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "due_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "due_time": forms.TimeInput(attrs={"type": "time"}, format="%H:%M"),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["category"].queryset = Category.objects.filter(user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        labels = {"title": "Kategori adı"}