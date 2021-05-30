from django.shortcuts import render
from .models import form1
from .forms import TestForm1
from .serializers import App1Serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import App1Serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseBadRequest

def main1(request):
	form = TestForm1(request.POST or None)
	if request.method == 'POST':
		instance = form.save(commit = False)
		print(instance.first_name, instance.last_name)
		if form.is_valid():
			form.save()
			print(form.cleaned_data.get("first_name"))
			print(form.cleaned_data.get("last_name"))

	return render(request, "form1.html", {"form": form})

def app1_details(request):
	fname = form1.objects.get()
	serializer = App1Serializer(fname)
	json_data = JsonRenders().render(serializer.data)
	return HttpResponse(json_data, content_type = 'application/json')
		