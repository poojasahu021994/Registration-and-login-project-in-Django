from django.shortcuts import render
from .models import Registration

def index(request):
    return render(request,'index.html')

def register(request):
        if request.method=='POST':
           print(request.POST)
           print(request.FILES)
           customer_name=request.POST.get('username')
           customer_Email=request.POST.get('email')
           customer_details=request.POST.get('detail')
           customer_Number=request.POST.get('phone')
           customer_DOB=request.POST.get('dob')
           customer_Volume=request.POST.get('volume')
           customer_Education=request.POST.get('subject')
           customer_Gender=request.POST.get('gender')
           customer_Image=request.FILES.get('profile-pic')
           customer_Resume=request.FILES.get('resume')
           password=request.POST.get('password')
           cpassword=request.POST.get('cpassword')
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
           print(password)
           print(cpassword)
           user=Registration.objects.filter(customer_Email=customer_Email)
           if user:
                x="Email already exist"
                return render(request,'register.html',{'msg':x})
           Registration.objects.create(customer_name=customer_name,customer_Email=customer_Email,customer_details=customer_details,customer_Number=customer_Number,customer_DOB=customer_DOB,customer_Volume=customer_Volume,customer_Education=customer_Education,customer_Gender=customer_Gender,customer_Image=customer_Image,customer_Resume=customer_Resume)
        else:
            return render(request,'register.html')
def login(request): 
    return render(request,'login.html')
