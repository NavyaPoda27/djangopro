from django import forms
class EmailForm(forms.Form):
    recipient_email = forms.EmailField(label='Recipient Email')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
