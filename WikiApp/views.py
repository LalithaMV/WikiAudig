from django.shortcuts import render
#from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import CustomUserCreationForm
#from forms import CustomUserCreationForm
# Create your views here.

def error_processor(request):
	if 'error' in request.session:
		return {'msg': request.session['error']}
	else:
		return {}
	
def front(request):
	c=RequestContext(request,{'foo':'bar',},[error_processor])
	if 'error' in request.session:
		del request.session['error']
	return render_to_response('WikiApp/session/front.html',c)
	
def logout(request):
	auth.logout(request)
	#return render_to_response('WikiApp/session/front.html')	
	return HttpResponseRedirect('/WikiApp')
	
def auth_view(request):
	username= request.POST.get('username','')
	password= request.POST.get('password','')
	user= auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/WikiApp/home')
	else:
		request.session['error'] = "Username and Password do not match.Try Again!"
		return HttpResponseRedirect('/WikiApp')
#Have not done auth.logout(request)	
def home(request):
	return render_to_response('WikiApp/session/home.html', {'full_name':request.user.first_name,'languages_known':request.user.languages_known})
	#return render_to_response('WikiApp/session/home.html', {'full_name':request.user.userprofile.Languages})

def register_user(request):
	if request.method == 'POST':
		form=CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/WikiApp/register_success')
	else:
		form= CustomUserCreationForm()
	return render(request,  'WikiApp/session/register.html', {
		'form': form,
	})
def register_success(request):
	return render_to_response('WikiApp/session/register_success.html')
	
def digitize(request):
	return render_to_response('WikiApp/AudioDigi/Digitize.html')

		
		
	
