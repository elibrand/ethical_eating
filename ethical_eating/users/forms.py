from django.forms import Form, CharField, TextInput, PasswordInput, EmailInput, Select, ChoiceField, IntegerField


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


class BMIForm(Form):
    FEET_CHOICES = list(zip(map(str, range(1, 9)), list(range(1, 9))))
    INCH_CHOICES = list(zip(map(str, range(0, 13)), list(range(0, 13))))
    feet = IntegerField(widget=Select(choices=FEET_CHOICES, attrs={
        'class': 'form-control w-50'
    }))
    inches = IntegerField(widget=Select(choices=INCH_CHOICES, attrs={
        'class': 'form-control w-50'
    }))
    weight = IntegerField(label='Weight in Pounds:', widget=TextInput(attrs={
        'class': 'form-control w-50'
    }))


def cal_height(feet, inches):
    """
    converts height in feet and inches into inches
    :return: height in inches
    """
    return (feet * 12) + inches


def cal_bmi(height, weight):
    """
    calculates bmi then rounds it to integer with one decimal point
    :param height: user's height in meters
    :param weight: user's weight in kg
    :return: bmi with one decimal
    """
    return round(weight / (height ** 2), 1)
