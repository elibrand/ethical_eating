from django import forms


class QuestionForm(forms.Form):
    ask = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-50'
    }))


class ReviewForm(forms.Form):
    CHOICES = list(zip(map(str, range(1, 11)), list(range(1, 11))))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control w-50'
    }))
    rating = forms.IntegerField(widget=forms.Select(choices=CHOICES, attrs={
        'class': 'form-control w-50'
    }))
    review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-50'
    }))
