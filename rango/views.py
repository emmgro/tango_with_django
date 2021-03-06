from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")

	# Construct a dictionary to pass to the template engine as its content.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
	
	# Return a rendered response to send to the client
	# We make use of the shortcut function to make our lives easier
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context = {'authors':'emmgro'}
	return render(request, 'rango/about.html', context=context)