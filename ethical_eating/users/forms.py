from django.forms import Form, CharField, TextInput, PasswordInput, EmailInput


class RegisterForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-50'
    }))
    email = CharField(label='Email', widget=EmailInput(attrs={
        'class': 'form-control w-50'
    }))
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))
    password = CharField(widget=PasswordInput(attrs={
        'class': 'form-control w-50'
    }))