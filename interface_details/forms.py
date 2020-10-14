from django import forms
from .models import router

class routerform(forms.ModelForm):

	class Meta:
		model = router
		fields = ['sapid', 'hostname', 'loopback', 'mac_address']
