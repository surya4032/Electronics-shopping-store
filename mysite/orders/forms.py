from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address_line1", "address_line2", "city", "state", "zip_code", "country"]
        widgets = {
            "address_line1": forms.TextInput(attrs={"class": "form-control",'required':True}),
            "address_line2": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control",'required':True}),
            "state": forms.TextInput(attrs={"class": "form-control",'required':True,'pattern':'[a-zA-Z]' ,'title': 'State must contain only alphabets'}),
            "zip_code": forms.TextInput(attrs={"class": "form-control",
            'required':True,
            'pattern': '[0-9]{6}',
            'title': 'PIN must be a 6-digit number'}),
            
            
            "country": forms.TextInput(attrs={"class": "form-control",'required':True}),
            # "country": forms.Select(attrs={"class": "form-control",'required':True}),
        }
    # def clean_pin(self):
    #     pin = self.cleaned_data.get('pin')
    #     if not pin.isdigit():
    #         raise forms.ValidationError("PIN must contain only digits.")
    #     return pin