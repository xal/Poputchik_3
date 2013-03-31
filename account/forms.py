from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='Name:', initial='')
    email = forms.EmailField(label='E-mail:', initial='')
    password = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password_check = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput)
    is_driver = forms.BooleanField(initial=False, required=False)
    coord_from = forms.CharField()
    coord_to = forms.CharField()

#class ProfileForm(forms.Form):
#    email = forms.EmailField(label='E-mail:', initial='')
#    first_name = forms.CharField(label='First Name:')
#    last_name = forms.CharField(label='Last Name:')
#    phone = forms.CharField(label='Phone:')
#    address_1 = forms.CharField(label='Address 1:')
#    address_2 = forms.CharField(label='Address 2:', required=False)
