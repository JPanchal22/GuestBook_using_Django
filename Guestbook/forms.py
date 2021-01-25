from django import forms

class commentForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class":"form-group", "placeholder":"Enter your name..."}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40,"class":"form-group", "placeholder":"Enter your comment..."}))
