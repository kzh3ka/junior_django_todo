from django import forms


class TaskForm(forms.Form):
    description = forms.CharField()
