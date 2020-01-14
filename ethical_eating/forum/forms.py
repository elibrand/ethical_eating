from django import forms


class ThreadForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-100'
    }))
    subject = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100'
    }))


class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-50'
    }))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-50'
    }))
