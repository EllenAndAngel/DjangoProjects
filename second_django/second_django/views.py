from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
	return HttpResponse("hello django!")

def hello_from_templates(request):
	return render(request,'hello.html')

def index(request):
	return render(request,'index.html')

def translate(request):
	original_text = request.GET['originaltext'].lower()
	originals = original_text.split()
	translation = ''

	for word in originals:
		if word[0] in ['a','e','i','o','u']:
			#vowels
			translation += word
			translation += 'yay '
		else:
			#constants
			translation += word[1:]
			translation += word[0]
			translation += 'ay '

	return render(request,'translate.html',
		{'original':original_text ,'translation':translation})

def about(request):
	return render(request,'about.html')