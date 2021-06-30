from django.db import models
import datetime

from django.db.models.fields import EmailField



# Create your models here.
class feed(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class subscriber(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(("Date"), default=datetime.datetime.today)

    def __str__(self):
        return self.email

class signup(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.EmailField()
    password=models.CharField(max_length=50)
    date = models.DateTimeField(("Date"), default=datetime.datetime.today)
    

    def __str__(self):
        return self.name

class usercreatesurvey(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class usereditsurvey(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class uquest(models.Model):
    email=models.EmailField(default=None)
    question=models.CharField(max_length=500)
    date = models.DateTimeField(("Date"), default=datetime.datetime.today)

    def __str__(self):
        return self.email
 
class edituser(models.Model):
    email_id=models.EmailField()
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class addsurvey(models.Model):
    EFFECT=(
        ('Effect-1','Effect-1'),
        ('Effect-2','Effect-2'),
        ('Effect-3','Effect-3'),
        ('Effect-4','Effect-4'),
        ('Effect-5','Effect-5'),
        ('Effect-6','Effect-6'),
        ('Effect-7','Effect-7'),
        ('Effect-8','Effect-8'),
        ('Effect-9','Effect-9'),
        ('Effect-10','Effect-10'),    
    )
    email=models.EmailField()
    name=models.CharField(max_length=50)
    footer=models.CharField(max_length=50)
    effect=models.CharField(max_length=50,choices=EFFECT)
    date = models.DateTimeField(("Date"), default=datetime.datetime.today)

    def __str__(self):
        return self.name

class uchp(models.Model):
    email=models.EmailField()
    oldpassword=models.CharField(max_length=50)
    newpassword=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.email

class adminsignup(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class add_testimonials(models.Model):
    STATUS=(
        ('Active','Active'),
        ('Inactive','Inactive'),
    )
    image=models.ImageField(upload_to="uploads/",null=True,blank=True)
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    status=models.CharField(max_length=100,choices=STATUS)

    def __str__(self):
        return self.name

class edit_testimonials(models.Model):
    image=models.ImageField(upload_to="uploads/",null=True,blank=True)
    name=models.CharField(max_length=50)

    designation=models.CharField(max_length=50)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class achp(models.Model):
    oldpassword=models.CharField(max_length=50)
    newpassword=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50)

    def __str__(self):
        return self.oldpassword