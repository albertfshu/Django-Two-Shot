from django import forms
from receipts.models import ReceiptForm


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = ReceiptForm
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]
