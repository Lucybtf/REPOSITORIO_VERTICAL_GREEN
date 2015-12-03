# Register your models here.

from django import forms
 
class PostForm(forms.Form):
	title = forms.CharField(max_length=100)
	url = forms.URLField()#campo de tipo url
	content = forms.CharField(widget=forms.Textarea)#campo de tipo textarea 