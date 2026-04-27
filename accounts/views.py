from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    if request.POST:
        data = request.POST
        fn = data['fname']
        ln = data['lname']
        un = data['username']
        ue = data['uemail']
        p1 = data['password']
        p2 = data['cpassword']
        if not all([fn,ln,un,ue,p1,p2]):
            messages.error(request,'All filds are requered',extra_tags="register")

        elif User.objects.filter(username = un).exists():
            messages.error(request,'Username is already used',extra_tags="register")

        elif User.objects.filter(email = ue).exists():
            messages.error(request,'E-mail is alreday used',extra_tags="register")

        elif p1 != p2:
            messages.error(request,"Password dosn't match" ,extra_tags='register')

        elif len(p1)<6:
            messages.error(request,'Password must be at least 6 characters',extra_tags="register")

        else: 
            User.objects.create_user(first_name = fn,last_name = ln ,username = un,email= ue,password= p1)
            messages.success(request,"Account created successfully",extra_tags="register")
            return redirect('login_p')

        return render(request, 'accounts/register.html', {

        'fname': fn,
        'lname': ln,
        'username': un,
        'email': ue,
        'password':p1,
        'cpassword':p2

        }) 

    return render(request, 'accounts/register.html', {
            'fname': '',
            'lname':'',
            'username': '',
            'email': '',
            'password': '',
            'cpassword':''
        })

def log_in(request):
    if request.method == 'POST':
        ue = request.POST.get('uemail')
        ps = request.POST.get('password')

        user_obj = User.objects.filter(email__iexact=ue).first()

        if user_obj:
            user = authenticate(request, username=user_obj.username, password=ps)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successfully", extra_tags="login")
                return redirect('homepage')
            else:
                messages.error(request, "Invalid password", extra_tags="login")
                return redirect('login_p')
        else:
            messages.error(request, "Email not found", extra_tags="login")


    return render(request, 'accounts/login.html',)

def log_out(request):
    logout(request)
    messages.success(request,"Logout succfully",extra_tags="logout")
    return redirect("homepage")



# def changepassword(request):
#      form = PasswordChangeForm(user= request.user)
#      if request.method == "POST":
#           form = PasswordChangeForm(user=request.user,data = request.POST)
#           if form.is_valid():
#                form.save()
#                messages.success(request,"Password change successfully")
#                return redirect('homepage')
          
#      return render(request,"accounts/changepassword.html",{"form":form})

