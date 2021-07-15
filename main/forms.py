from django import forms


class atomicnameform(forms.Form):
    q = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={
        'class':'form-control addpadding', 'aria-label':"Recipient's username","type":"text","placeholder":"Search with name ,number or symol","aria-describedby":"button-addon2","name":"q"
    }))


