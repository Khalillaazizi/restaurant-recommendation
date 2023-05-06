from django.forms import ModelForm, Textarea
from .models import Review,Restaurant,Category
from django import forms
from .models import User


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'review_title',
            'review_description',
        ]
        widgets = {
            'review_description': Textarea(attrs={'cols': 80, 'rows': 8}),
        }

class RestaurantForm(forms.ModelForm):
    restaurant_text= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
    restaurant_address= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))   
    class Meta:
        model = Restaurant
        fields = '__all__'
