from django.shortcuts import render,redirect

from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = SignUpForm()
    form.order_fields(field_order=['name','last_name','role','username','email','password1','password2'])
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()

            print(user)
            #auth_login(request,user)
            new_user = User.objects.create(
                user = user,
                name=form.cleaned_data.get('name'),
                role=form.cleaned_data.get('role'),
            )
            messages.success(request, 'The user has been created successfully.')
            return redirect('admin')

    return render(request,'admin/gestutil.html',{'form':form})

@login_required
def gestion(request):
    return render(request,'admin/gestion.html')


@login_required
def rappstas(request):
    return render(request,'admin/rappstas.html')

@login_required
def securité(request):
    return render(request,'admin/securité.html')

@login_required
def surveil(request):
    return render(request,'admin/surveil.html')

@login_required
def etatdedem(request):
    return render(request,'employer/etatdedem.html')

@login_required
def info(request):
    return render(request,'employer/info.html')

@login_required
def notif(request):
    return render(request,'employer/notif.html')

@login_required
def prodem(request):
    return render(request,'employer/prodem.html')

@login_required
def assistance(request):
    return render(request,'help disk/assistance.html')

@login_required
def connaissance(request):
    return render(request,'help disk/connaissance.html')

@login_required
def demand(request):
    return render(request,'help disk/demand.html')

@login_required
def redirection(request):
    return render(request,'help disk/redirection.html')

@login_required
def comm(request):
    return render(request,'technicien/comm.html')

@login_required
def GPI(request):
    return render(request,'technicien/GPI.html')


@login_required
def GTA(request):
    return render(request,'technicien/GTA.html')

@login_required
def ticket(request):
    return render(request,'technicien/ticket.html')



@login_required
def tech(request):
    role = User.objects.filter(user=request.user)
    role = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'technicien':
        return render(request,'technicien/technicien.html',{'x':role})
    else:
        return render(request,'404.html')

@login_required
def help_desk(request):
    username = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'help desk':
        return render(request,'help disk/help.html',{'username':username})
    else:
        return render(request,'404.html')

@login_required
def employer(request):
    username = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'employer':
        return render(request,'employer/employe.html',{'username':username})
    else:
        return render(request,'404.html')

@login_required
def admin(request):
    username = request.user
    #print(role.objects.get(role))
    role = User.objects.filter(user=request.user).values('role')
    if role[0]['role'] == 'admin':
        return render(request,'admin/admin.html',{'username':username})
    else:
        return render(request,'404.html')



class MyLoginView(LoginView):

    def get_success_url(self):
        role = User.objects.filter(user=self.request.user).values('role')
        if role[0]['role'] == 'technicien':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_TECH)
        elif role[0]['role'] == 'help desk':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_HD)
        elif role[0]['role'] == 'employer':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_EMP)
        elif role[0]['role'] == 'admin':
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL_ADMIN)


# def login(request):

#     form = AuthenticationForm()
#     if request.method =='POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             print(form)
#             user = form.save()
#             print(user)
#             auth_login(request,user)

#             return redirect('login')

#     """
#     if ....
#         redirect to ...
    
    
#     """
    

#     return render(request,'index/index.html',{'form':form})