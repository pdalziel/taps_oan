from django import forms
from django.contrib.auth.models import User 
from taps_oan.models import Pub, Beer, UserProfile

class PubForm(forms.ModelForm):
	name = forms.CharField(max_length=128, 
							help_text="Please enter the pub name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Pub
		fields = ('name',)

class BeerForm(forms.ModelForm):
	title = forms.CharField(max_length=128, 
						help_text="Please enter the title of the beer.")
	url = forms.URLField(max_length=200, 
						help_text="Please enter the URL of the beer.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	class Meta:
		model = Beer

		exclude = ('pub',)

	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		# If url is not empty and doesn't start with 'http://', 
		# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

			return cleaned_data

class UserForm(forms.ModelForm): 
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('website', 'picture')