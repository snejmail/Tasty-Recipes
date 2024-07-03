from django import forms

from users.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']

        widgets = {
            'password': forms.PasswordInput(),
            'chef': forms.CheckboxInput(attrs={'checked': False})
        }
        error_messages = {
            'nickname': {
                'min_length': "Nickname must be at least 2 characters long!"
            },
            'first_name': {
                'invalid': "Name must start with a capital letter!"
            },
            'last_name': {
                'invalid': "Name must end with a capital letter!"
            },
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()