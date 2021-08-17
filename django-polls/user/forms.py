from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields=['username','password1','password2','nickname','location','university']
'''
class UserForm(AbstractUser): 
    class Meta:  
        model = CustomUser
        fields=['username','password1','password2','nickname','location','university']'''