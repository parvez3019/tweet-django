from django import forms
from .models import tweet_text
class StatusForm(forms.ModelForm):
	class Meta:
		model=tweet_text
		fields=['text']
def clean_text(self):
	text=self.cleaned_data.get('text')
	return text