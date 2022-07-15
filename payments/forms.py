from pyexpat import model
from django import forms
from payments.models import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('email', 'amount')
