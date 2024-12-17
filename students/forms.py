from django import forms
from .models import Student
from .models import Dish

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'faculty', 'gpa']

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['student', 'dish', 'quantity']