from django import forms

class CoverForm(forms.Form):
    title = forms.CharField()
    top_text = forms.CharField()
    author = forms.CharField()
    animal_code = forms.IntegerField()
    color_code = forms.IntegerField()
    guide_text = forms.CharField()
    guide_text_piacement = forms.CharField()