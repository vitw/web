from django import forms



class CommentForm(forms.Form):
	text = forms.CharField(label = 'Your comment',max_length = 200)
