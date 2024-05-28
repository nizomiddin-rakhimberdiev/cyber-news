from django import forms

from cyber.models import GameCommentary, Gamer


class GameCommentaryForm(forms.ModelForm):
    # pass
    class Meta:
        model = Gamer
        fields = ('username', 'rating', 'avatar', 'game', 'password')