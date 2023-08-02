from django.shortcuts import redirect,render

from django.http import HttpResponse

from  django.contrib.auth.models import User

from django.contrib import messages

from django.shortcuts import redirect,render

from django.contrib.auth import  authenticate , login, logout

from user import settings

from django.core.mail import send_mail

from django.contrib.sites.models  import Site

from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode

from django.utils.encoding import force_bytes,force_str

from . tokens import generate_token

from django.core.mail import send_mail

# Create your views here.

def home(request):

    return 	render(request,"login/home.html")


def signin(request):

    if request.method=='POST':

        username=request.POST["username"]

        password=request.POST["password"]


        user=authenticate(username=username,password=password)


        if user is not None:

            login(request,user)

            fname=user.first_name
            messages.info(request,'Welcome '+str(fname))


            return render(request,"authentication/home.html",{'fname':fname})

        else:

            message(request,"Bad Credntials")

    return redirect('home')    
        
        



    return 	render(request,"login/signin.html")


def signout(request):

    logout(request)

    message.success(request,"loggedout successfully")

    return  redirect('home')

def jls_extract_def():
    return 'lname'


def signup(request):


    if request.method=="POST":

        username=request.POST["username"]

        fname=request.POST["fname"]
        lname=""

       

        email=request.POST["email"]

        password=request.POST["password"]
        confirm_passowrd = request.POST['confirm_password']

       
        # print(f"Username: {username}, First Name:{fname} Last name :{lname}")


        if User.objects.filter(username=username):

            error="This Username already exists!"

            messages.error(request,"This Username already exists!")

            return redirect('home')



        if User.objects.filter(email=email):

            error="This email already exists!"

            messages.error(request,"This email already exists!")

            return redirect('home')

        if len(username)>10:

            messages.error(request,"username must be ten chracters")

        if password != confirmpassword:

            messages.error(request,"password doestn't match")

        if not username is alnum():

            messages.error(request,"username must be contains alphabets and numbers")

            return redirect('home')


        myuser=User.objects.create_user(username,email,password)

        myuser.first_name=fname

        myuser.last_name=lname

        myuser.is_active=False


        myuser.save()

        messages.success(request,"account created successfully")


        subject="welcome to PGS"

        message="Hello" + myuser.first_name + "!! \n  " +"Welcome to PGS \n thankyou for visiting our websie \n we also sen a conformation email please confirm your email "

        from_email=settings.EMAIL_HOST_USER

        to_list=[myuser.email]

        send_mail(subject,message,from_email,to_list,fail_silently=True)
        

        current_sites=get_current_sites(request)

        email_subject="confirm email  @PGS  !"
       

        message2=render_to_string('email_confirmation.html',{

            'name':myuser.first_name,

            "domain":current_site.domain,

            "uid":urlsafe_base64_encode(force_bytes(myuser.

            pk)),

            'token':generate_token.make_token(myuser)


        })
        

        email.fail_silently=True
        email.send()


        return redirect("signin.html")

    return render(request,"login/signup.html")


def activate(request,uidb64,token):

    try:

        uid=force_text(urlsafe_base64_encode)

        myuser=User.objects.get(pk=uid)

    except (TypeError,ValueError,OverflowError,User.DoesNotExist):

        myuser=None

    if myuser is not None and generate_token.check_token(myuser, token):

        myuser.is_active=True

        myuser.save()

        login(request,myuser)

        messages.success(request, "Your Account has been activated successfully!")

        return redirect('home')

    else:


            messages.error(request, "Invalid Activation Link.")
             



            

