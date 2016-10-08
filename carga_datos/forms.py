from django import forms

class UploadForm(forms.Form):
	nombre_archivo = forms.CharField(max_length=100)
	ubicacion_archivo = forms.FileField(
        label='Selecciona un archivo'
    )