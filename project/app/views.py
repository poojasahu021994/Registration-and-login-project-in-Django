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
           else:
                if password==cpassword:
                    Registration.objects.create(customer_name=customer_name,customer_Email=customer_Email,customer_details=customer_details,customer_Number=customer_Number,customer_DOB=customer_DOB,customer_Volume=customer_Volume,customer_Education=customer_Education,customer_Gender=customer_Gender,customer_Image=customer_Image,customer_Resume=customer_Resume,password=password)
                    x="Registration Sucessfully"
                    return render(request,'login.html',{'msg':x})
                else:
                    x="password and confirm password not match"
                    return render(request,'register.html',{'msg':x,'name':customer_name,'customer_Email':customer_Email,'customer_details':customer_details,'customer_Number':customer_Number,'customer_DOB':customer_DOB,'customer_Volume':customer_Volume,'customer_Gender':customer_Gender,'customer_Image':customer_Image,'customer_Resume':customer_Resume,'password':password})          
        else:
            return render(request,'register.html')
def login(request): 
    if request.method=='POST':
         email=request.POST.get('email')
         password=request.POST.get('Password')
         user=Registration.objects.filter(customer_Email=email)
         print(user)
         if user:
              data=Registration.objects.get(customer_Email=email)
              user_data={
                  'name':data.customer_name,
                  'email':data.customer_Email,
                  'details':data.customer_details,
                  'DBO':data.customer_DOB,
                  'number':data.customer_Number,
                  'educatio':data.customer_Education,
                  'gender':data.customer_Gender,
                  'image':data.customer_Image,
                  'volume':data.customer_Volume,
                  'resume':data.customer_Resume,
                  'password':data.password,
                  }
              print(user_data)
              pass1=data.password
              print(pass1,password)
              if pass1==password:
                   return render(request,'dashboard.html',{'name':data.customer_name,'email':data.customer_Email,'data':user_data})
                    #  return redirect('dashboard')
              else:
                   x="Email and password not match"
                   return render(request,'login.html',{'msg':x})
              
         else:
              x="Email id not exist"
              return render(request,register,'register.html',{'msg':x})
    else:
         return render(request,'login.html')
# 