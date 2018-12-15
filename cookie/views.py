from django.shortcuts import render
from .models import Student
from .models import Contact
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request,'index.html')

def insert(request):
    if request.method=="POST":
        try:
            user=Student.objects.get(username=request.POST["name"])
            if user:
               return render(request,'index.html',{"message":"user already exist"})
        except Student.DoesNotExist:
            newuser=Student(username=request.POST["name"],email=request.POST["Email"],password=make_password(request.POST["Password"]))
            newuser.save()
            return render(request,'index.html')

def user_login(request):
        username=request.POST["name"]
        password=request.POST["Password"]
        try:
            dbuser=Student.objects.get(username=username)
            if check_password(password, dbuser.password):
                return render(request,'update.html',{'username':dbuser.username})
            else:
                return render(request,'index.html',{"message1":"invalid passward enter"})
        except Student.DoesNotExist:
            return render(request,'index.html',{"message1":"name  does not exist"})


def contact(request):
    Firstname1=request.GET["email1"]
    Lastname1=request.GET["name"]
    Mobile1=int(request.GET["email"])
    Email1=request.GET["email12"]
    Yourmessage1=request.GET["area"]
    g=Contact(Firstname=Firstname1,Lastname=Lastname1,Mobile=Mobile1,Email=Email1,Yourmessage=Yourmessage1)
    g.save()
    return render(request,'index.html')




"""username1=request.POST["name"]
    email1=request.POST["Email"]
    password1=make_password(request.POST["Password"])"""




"""f = Student(username=username1, email=email1, password=password1)
    f.save()
    return render(request, 'index.html')"""




"""try:
        user=Student.objects.get(username=username1)
    except:
      return  user.DoesNotExist
      raise forms.ValidationError(u'Username "%s" is already in use.' % username)"""








"""f=Student(username=username1,email=email1,password=password1)
    f.save()
    return render(request,'index.html')
 try:
   user = User.objects.get(username=username)
 except user.DoesNotExist:
    return username1
    raise forms.ValidationError(u'Username "%s" is already in use.' % username)"""


"""def user_login(request):
        USERNAME = request.POST["name"]
        PASSWORD= request.POST['Password']
        dbuser = Student.objects.filte(name=USERNAME, Password=PASSWORD)
        if not  dbuser:
            return HttpResponse("error")
        else:
            return render(request, 'index.html', )"""


"""def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
         USERNAME= request.POST["name"]
         PASSWORD = request.POST["Password"]
         user = authenticate(name=USERNAME, Password=PASSWORD)
         if user is not None:
              if user.is_active:  
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("index.html")
              else:
                  # Return a 'disabled account' error message
                 return HttpResponse("You're account is disabled.")
         else:
              # Return an 'invalid login' error message.
              print("invalid login details " + USERNAME + " " + PASSWORD)"""



"""def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index.html")"""

"""if not dbuser:
    print("error")
    return HttpResponse("error")
elif check_password(password, dbuser.password):
    return render(request, 'index.html')
else:
    return HttpResponse("passwod missmatch")"""