# -*-coding:Utf-8 -*
""" définition des formulaires """
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """ définition du formulaire pour les commentaires """
    class Meta:
        """"meta pour le formulaire"""
        model = Comment
        #fields = '__all__'
        fields = ('pseudo', 'email', 'contenu')
            