from django import forms

class atomicnumberform(forms.Form):
    value = forms.IntegerField(min_value=1,max_value=118,label="",widget=forms.TextInput(attrs={
        'class':'form-control addpadding', 'aria-label':"Recipient's username","type":"number","placeholder":"Atomic Number","aria-describedby":"button-addon2"
    }))
    key=forms.CharField(label="",widget=forms.TextInput(attrs={
        "value":"atomicNumber","style":"display:none;"
    }))

class atomicnameform(forms.Form):
    value = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={
        'class':'form-control addpadding', 'aria-label':"Recipient's username","type":"text","placeholder":"Atomic Name","aria-describedby":"button-addon2"
    }))
    key=forms.CharField(label="",widget=forms.TextInput(attrs={
        "value":"name","style":"display:none;"
    }))

class atomicsymbolform(forms.Form):
    value = forms.CharField(max_length=3,label="",widget=forms.TextInput(attrs={
        'class':'form-control addpadding', 'aria-label':"Recipient's username","type":"text","placeholder":"Atomic Symbol","aria-describedby":"button-addon2"
    }))
    key=forms.CharField(label="",widget=forms.TextInput(attrs={
        "value":"symbol","style":"display:none;"
    }))

class numberclicked(forms.Form):
    clickednumber= forms.IntegerField(label="",widget=forms.TextInput(attrs={
        "type":"hidden","value":"2"
    }))

class nameclicked(forms.Form):
    clickednumber= forms.IntegerField(label="",widget=forms.TextInput(attrs={
        "type":"hidden","value":"1"
    }))

class symbolclicked(forms.Form):
    clickednumber= forms.IntegerField(label="",widget=forms.TextInput(attrs={
        "type":"hidden","value":"3"
    }))



