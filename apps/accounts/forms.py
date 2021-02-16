from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2", "profile_pic")
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
