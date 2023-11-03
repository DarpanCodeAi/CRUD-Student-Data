from django import forms
from .models import Employee

class UpdateEmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ['firstname','lastname','semester','age','department'] 
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname' :  forms.TextInput(attrs={'class':'form-control'}),
            'semester' :  forms.Select(attrs={'class':'form-control'}),  
            'age' :  forms.NumberInput(attrs={'class':'form-control'}),
            'department' :  forms.TextInput(attrs={'class':'form-control'}),

            
        } 