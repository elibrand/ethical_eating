from django import forms

from resources.models import Question, Questions


class QuestionForm(forms.Form):
    ask = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control w-100'
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


class QuizForm(forms.Form):
    q = Question.objects.all().order_by('id')
    q1 = forms.ModelChoiceField(label=q[0].text,
                                queryset=q[0].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q2 = forms.ModelChoiceField(label=q[1].text,
                                queryset=q[1].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q3 = forms.ModelChoiceField(label=q[2].text,
                                queryset=q[2].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q4 = forms.ModelChoiceField(label=q[3].text,
                                queryset=q[3].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q5 = forms.ModelChoiceField(label=q[4].text,
                                queryset=q[4].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q6 = forms.ModelChoiceField(label=q[5].text,
                                queryset=q[5].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q7 = forms.ModelChoiceField(label=q[6].text,
                                queryset=q[6].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q8 = forms.ModelChoiceField(label=q[7].text,
                                queryset=q[7].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)
    q9 = forms.ModelChoiceField(label=q[8].text,
                                queryset=q[8].choices.all(),
                                widget=forms.RadioSelect,
                                empty_label=None)


