from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"your name"})
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Leave your comment!"})
    )
    
class PostForm(forms.Form):
    title=forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class":"form-control1","placeholder":"Post Title"}),
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control1","placeholder":"Create Your Post"}),
    )