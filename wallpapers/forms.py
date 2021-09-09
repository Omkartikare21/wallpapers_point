from django import forms
from django.db.models import fields
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["user_name", "user_email", "text"]
        labels = {
            "user_name": "Name",
            "user_email": "Email",
            "text": "Comment"
        }
