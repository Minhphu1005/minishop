from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label='Họ')
    last_name = forms.CharField(max_length=30, required=False, label='Tên')
    email = forms.EmailField(required=False, label='Email')
    
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'postal_code']
        labels = {
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ',
            'city': 'Thành phố',
            'postal_code': 'Mã bưu điện',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
        
        for field in ['first_name', 'last_name', 'email']:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            # Update User model fields
            user = profile.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.save()
            profile.save()
        return profile
