from django import forms
from django.core.validators import validate_email,MaxLengthValidator,MinLengthValidator
from .models import ReuqestList, YourLogin
CHOICES= [
    ('mharastra', 'mharastra'),
    ('Rajasthan', 'Rajasthan'),
    ('udaypur', 'udaypur'),
    ('hariyana', 'hariyana'),
    ]



class YourLoginForm(forms.Form):
   username = forms.CharField(max_length=254,validators=[validate_email],required = True)
   password = forms.CharField(max_length=254,label=("Password"), widget=forms.PasswordInput,required = True) 
    
class YourLoginRegisterform(forms.ModelForm):
   class Meta:
      model = YourLogin
      fields = '__all__'
   password = forms.CharField(widget=forms.PasswordInput)
   Repassword = forms.CharField(widget=forms.PasswordInput)
   
class ReuqestListForm(forms.ModelForm):
   class Meta:
      model = ReuqestList
      fields = '__all__'




