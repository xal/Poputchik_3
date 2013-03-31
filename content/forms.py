from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name:')
    company = forms.CharField(label='Company:', required=False)
    address = forms.CharField(label='Address:', required=False)
    email = forms.EmailField(label='E-mail:')
    phone = forms.CharField(label='Phone:')
    fax = forms.CharField(label='Fax:')
    message = forms.CharField(label='Message:', widget=forms.Textarea, required=True)
