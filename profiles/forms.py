from django import forms
from profiles.models import UserProfile

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('height', 'weight', 'goals', 'photo')

    # def __init__(self, *args, **kwargs):
    #     super(ProfileRegistrationForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        instance = super(ProfileRegistrationForm, self).save(commit=True)

        if commit:
            instance.save()

        return instance