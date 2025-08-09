import re
from django import forms
from .models import Tweet

BANNED_WORDS = ['shit', 'fuck', 'bobo']

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': "What's happening?"
            })
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        # \b word boundaries; case-insensitive; handles punctuation like "shit!" or "(fuck)"
        pattern = r'\b(' + '|'.join(re.escape(w) for w in BANNED_WORDS) + r')\b'
        if re.search(pattern, content, flags=re.IGNORECASE):
            raise forms.ValidationError(
                "Your tweet contains banned words. Please remove offensive words."
            )
        return content
