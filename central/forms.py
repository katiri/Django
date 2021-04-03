from django import forms

class FormCadastro(forms.Form):
    nome_usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    primeiro_nome = forms.CharField()
    ultimo_nome = forms.CharField()

class FormLogin(forms.Form):
    nome_usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput)

class FormChangeSenha(forms.Form):
    senha_antiga = forms.CharField(widget=forms.PasswordInput)
    senha_nova = forms.CharField(widget=forms.PasswordInput)
    senha_nova_conf = forms.CharField(widget=forms.PasswordInput)