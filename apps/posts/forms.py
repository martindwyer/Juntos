from django import forms
from django.forms import Textarea
from apps.posts import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "post_picture", "group")
        model = models.Post
        widgets = {
            'message': Textarea(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                models.Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )
