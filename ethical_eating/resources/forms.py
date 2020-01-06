from django import forms


class QuestionForm(forms.Form):
    ask = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-50'
    }))
