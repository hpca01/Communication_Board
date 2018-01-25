from django import forms
from .models import Comm_Item, comment

class CommForm(forms.ModelForm):

	class Meta:
		model = Comm_Item
		fields = ('comm_type', 'title', 'descr',)
		labels = {
            'comm_type': ('Type of Communication'),
            'title': ('Title'),
            'descr': ('Details'),
        }

class comment_form(forms.ModelForm):

	class Meta:
		model = comment
		fields = {'content',}
		labels = {
			'content':('Comment'),
		}