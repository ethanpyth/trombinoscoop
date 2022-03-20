from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            if password != 'sesame' or email != 'pierre@lxs.be':
                raise forms.ValidationError("Adresse de courriel ou mot de passe érroné")
            return cleaned_data
