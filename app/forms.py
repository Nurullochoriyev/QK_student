
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['familya', 'ismi', 'otasini_ismi', 'tel_raqami', 'adres','fan']
        widgets = {
            'familya': forms.TextInput(attrs={'class': 'form-control'}),
            'ismi': forms.TextInput(attrs={'class': 'form-control'}),
            'otasini_ismi': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_raqami': forms.TextInput(attrs={'class': 'form-control'}),
            'adres': forms.TextInput(attrs={'class': 'form-control'}),
            'fan': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'familya': 'Familiya',
            'ismi': 'Ismi',
            'otasini_ismi': 'Otasini ismi',
            'tel_raqami': 'Telefon raqami',
            'adres': 'Manzil',
            'fan':'fan',
        }
from django import forms
from .models import Fan

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Fan nomi',
        }