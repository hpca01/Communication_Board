from django import template
from django.contrib.auth.models import User


register = template.Library()

@register.filter(name='get_usn')
def get_username(value):
	user = User.objects.get(pk=value)
	return user.username