from django import forms

from myapp.models import Portfolio

class createNewItemAbout(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class':'input'}))

class createNewService(forms.Form):
    icon = forms.CharField(label="Nombre del icono", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    title = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion del servicio", widget=forms.Textarea(attrs={'class':'input'}))
    
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'image']

    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),  max_length=50)
    description = forms.CharField (widget=forms.Textarea(attrs={"class":"form-control"}), max_length=100)
    image = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={'class':'form-control'}))


class NewContact(forms.Form):
    name = forms.CharField( max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'type': 'text','placeholder':"Nombre"}))
    email = forms.CharField( max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'type': 'email', 'placeholder':'Correo electronico'}))
    subject = forms.CharField( widget=forms.Textarea(attrs={'class':'input', 'type': 'text', 'placeholder':"Asunto"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class':'input', 'type': 'text', 'placeholder':"Mensaje"}))
