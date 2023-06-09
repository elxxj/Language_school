from django import forms
from django.contrib.auth.models import User
from .models import Student
from .models import Review


class StudentRegistrationForm(forms.Form):
    """
    Jest to formularz rejestracji studenta do szkoły językowej
    """
    name = forms.CharField(max_length=50, label='Imię')
    surname = forms.CharField(max_length=50, label='Nazwisko')
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Hasło')
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Potwierdź hasło')

    def clean(self):
        """
        Czyści dane w formularzu i sprawdza poprawność wprowadzonego hasła
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Hasła nie są identyczne.')

    def save(self):
        """
        Tworzy użytkownika - studenta
        """
        name = self.cleaned_data['name']
        surname = self.cleaned_data['surname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        student = Student.objects.create(name=name, surname=surname)
        user = User.objects.create_user(username=username, password=password)
        student.user = user
        student.save()


class ReviewForm(forms.ModelForm):
    """
    Jest to formularz dodawania opinii
    """
    class Meta:
        model = Review
        fields = ['text']
