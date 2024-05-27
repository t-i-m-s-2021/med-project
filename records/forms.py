from records.models import Record, Image
from django import forms

class addRecord(forms.ModelForm):
    choices = [
        ("кожа", "кожа"),
        ("легкие (ТАБ)", "легкие (ТАБ)"),
        ("лимфоузлы", "лимфоузлы"),
        ("молочная железа", "молочная железа"),
        ("мягкие ткани", "мягкие ткани"),
        ("моча", "моча"),
        ("поджелудочная железа (ЭУС)", "поджелудочная железа (ЭУС)"),
        ("гинекология (шейка матки)", "гинекология (шейка матки)"),
        ("щитовидная железа", "щитовидная железа"),
        ("жидкости", "жидкости"),
    ]

    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО', 'id': 'title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите описание', 'id': 'desc'}))
    localisation = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'placeholder': 'Выберите локализацию'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'id': 'employee'}))
    visible = forms.BooleanField(required=False)

    class Meta:
        model = Record
        fields = ['fullname', 'description', 'author', 'localisation', 'visible']

class addImage(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Image
        fields = ['image']

