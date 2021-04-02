from django import forms

class FormCadastro(forms.Form):
    nome_usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    primeiro_nome = forms.CharField()
    ultimo_nome = forms.CharField()