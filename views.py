from django.http import HttpResponse
form django.shortcuts import redirect
def index(request):
	return HttpResponse('index')
		
def login(requets):
	return redirect('/index')


