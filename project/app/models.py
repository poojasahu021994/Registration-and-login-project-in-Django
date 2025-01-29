from django.db import models

class Registration(models.Model):
    customer_name=models.CharField(max_length=50,help_text="Enter your name")
    customer_Email=models.EmailField()
    customer_details=models.CharField(max_length=100, help_text="Enter your details")
    customer_Number=models.IntegerField(help_text="Enter your Number")
    customer_DOB=models.DateField(help_text="Enter your DOB")
    customer_Volume=models.IntegerField()
    education=[('B.Tech','B.Tech'),('M.Tech','M.Tech'),('P.Hd','P.Hd')]
    customer_Education=models.CharField(max_length=50,choices=education)
    gender=[('Male','Male'),('Female','Female')]
    customer_Gender=models.CharField(max_length=50,choices=gender)
    customer_Image=models.ImageField(upload_to='image/')
    customer_Resume=models.FileField(upload_to='file/')
    password= models.CharField(max_length=50)
    cpassword= models.CharField(max_length=50)
    def __str__(self):
        return self.customer_name



# Create your models here.
