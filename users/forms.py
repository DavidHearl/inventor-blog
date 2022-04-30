from django import forms

class UserDeleteForm(forms.Form):
    """ Provides a check box """
    delete = forms.BooleanField(required=True)