from django import forms
from .models import Journey
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class journery_init(forms.ModelForm):
    # title = forms.CharField(label=(u'Task name'))
    # description = forms.CharField(label=(u'Task description'))
    # url_start = forms.CharField(label=(u'Start page url'))
    # url_end = forms.CharField(label=(u'Final page url'))

    def __init__(self, *args, **kwargs):
        super(journery_init, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = '/currentjourney/'
        # self.helper.layout.append()
        self.helper.layout.append(Submit('save', 'Start Journey'))

    class Meta:
        model = Journey
        fields = "__all__"
        exclude = ('Distance', "Driver", "JourneyStatus", "EndTime", "premium")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     # class Meta:
#     #     model = User
#     #     fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
#     #
#     #     def save(self, commit=True):
#     #         user = super(RegistrationForm, self).save(commit=False)
#     #         user.first_name = cleaned_data['first_name']
#     #         user.last_name = cleaned_data['last_name']
#     #         user.email = cleaned_data['email']
#     #
#     #         if commit:
#     #             user.save()
#     #         return user
