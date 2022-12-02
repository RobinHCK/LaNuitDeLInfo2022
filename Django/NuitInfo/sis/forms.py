from django import forms

class ImageGeneratorForm(forms.Form):
    sentence     = forms.CharField(label="Courte description de l\'image:", max_length=200)
    text_overlay = forms.CharField(label="Le texte du même:", max_length=200)

