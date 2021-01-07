from django.shortcuts import render,redirect
from project import settings 
from django.http import HttpResponse
from online_grocery.forms import Usregis,Upd,Pad
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from online_grocery.models import Exfd
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def showslides(request):
	return render(request,'home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			# print(rc)
			sb = "Online-grocery"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
			# print(p.username,p.email)
	y = Usregis()
	return render(request,'html/register.html',{'t':y})


@login_required
def prfle(request):
 	return render(request,'html/profile.html')


@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'html/upfle.html',{'r':p,'q':t})
	

@login_required
def products(request):
	return render(request,'html/products.html')

@login_required
def vegetables(request):
	return render(request,'html/vegetables.html')

@login_required
def fruits(request):
	return render(request,'html/fruits.html')

@login_required
def dairy(request):
	return render(request,'html/dairy.html')

@login_required
def pulses(request):
	return render(request,'html/pulses.html')

@login_required
def house(request):
	return render(request,'html/house.html')

@login_required
def care(request):
	return render(request,'html/care.html')

@login_required
def cart(request):
	return render(request,'html/cart.html')