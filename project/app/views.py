from django.shortcuts import render
from .models import Registration

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        pass
    else:
        return render(request,'register.html') 
    
def data(requset):
    print(requset.method)
    print(requset.POST)
    print(requset.FILES)

    customer_name=requset.POST.get('username')
    customer_Email=requset.POST.get('email')
    customer_details=requset.POST.get('detail')
    customer_Number=requset.POST.get('phone')
    customer_DOB=requset.POST.get('dob')
    customer_Volume=requset.POST.get('volume')
    customer_Education=requset.POST.get('subject')
    customer_Gender=requset.POST.get('gender')
    customer_Image=requset.FILES.get('profile-pic')
    customer_Resume=requset.FILES.get('resume')
    passwaod=requset.POST.get('password')
    cpassword=requset.POST.get('cpassword')
    
    print(customer_name)
    print(customer_Email)
    print(customer_details)
    print(customer_Number)
    print(customer_DOB)
    print(customer_Volume)
    print(customer_Education)
    print(customer_Gender)
    print(customer_Image)
    print(customer_Resume)
    print(passwaod)
    print(cpassword)
    Registration.objects.create(customer_name=customer_name,customer_Email=customer_Email,customer_details=customer_details,customer_Number=customer_Number,customer_DOB=customer_DOB,customer_Volume=customer_Volume,customer_Education=customer_Education,customer_Gender=customer_Gender,customer_Image=customer_Image,customer_Resume=customer_Resume,passwaod=passwaod,cpassword=cpassword)

def login(request): 
    return render(request,'login.html')
# Create your views here.