from django import forms
from .models import Journey, Profile, CompanyProfile
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
        exclude = ('Distance', "Driver", "JourneyStatus", "EndTime", "premium",'Duration')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        # self.helper = FormHelper(self)
        # self.helper.form_method = 'post'
        # self.helper.form_action = '/welcome/'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class profile_update(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('Surname', css_class='form-group col-md-4 mb-0'),
                Column('FirstName', css_class='form-group col-md-4 mb-0'),
                Column('LastName', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'NationalID','Gender','company','Role',
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Profile
        fields = ('Surname', 'FirstName', 'LastName', 'NationalID', 'Gender', 'company', 'Role')
