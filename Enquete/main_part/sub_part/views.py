from django.shortcuts import redirect, render
from . models import feed, subscriber
from . models import signup
from . models import usercreatesurvey
from . models import usereditsurvey
from . models import uquest
from . models import uchp
from . models import adminsignup
from . models import edituser
from . models import addsurvey
from . models import edit_testimonials
from . models import add_testimonials
from . form import ImageForm
# from . form import EdituserForm

from . models import achp
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
from django.contrib.auth import logout as log1
from django.conf import settings
from django.core.mail import send_mail


import easygui
import emoji

multi_user_name = ''
user_current_password = ''
user_current_id = ''
multi_admin_name = ''
admin_current_password = ''
admin_current_id = ''


# Create your views here.
def index(request):
    return render(request,'landing/index.html')

def index_feed(request):
    if request.method=='POST':
        if feed.objects.filter(name=request.POST['name'],
                               email=request.POST['email'],
                               subject=request.POST['subject'],
                               message=request.POST['message']
                              ):
            easygui.msgbox("Already Submitted",title="ENQUETE")
        else:
            if request.method=='POST':
                feed_dis=feed(name=request.POST['name'],
                              email=request.POST['email'],
                              subject=request.POST['subject'],
                              message=request.POST['message']
                              )
                feed_dis.save()
                easygui.msgbox("Thank You for your valuable feedback!!...",title="ENQUETE")
                return redirect(index)

    return render(request,'landing/index.html')

def index_subs(request):
    if request.method=='POST':
        if subscriber.objects.filter(email=request.POST['email']):
            easygui.msgbox("Already Subscribed!...")
            return redirect(index)
        else:
            if request.method=='POST':
                subs=subscriber(email=request.POST['email'])
                subs.save()
                # easygui.msgbox("Subscribed Successfully!...")
                return redirect(index)
    
    return render(request,'landing/index.html')

def login(request):
    if request.method=='POST':
        if signup.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
            check=signup.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
            global multi_user_name
            global user_current_password
            global user_current_id
            multi_user_name=check.name
            user_current_password=check.password
            user_current_id=check.id
            ut_data=signup.objects.get(name=multi_user_name)
            curr_pass=signup.objects.get(password=user_current_password)
            curr_id=signup.objects.get(id=user_current_id)
            easygui.msgbox("Loggedin successfully!!",title="ENQUETE")
            return redirect(survey)
            # return render(request,'dashboard/user/survey.html')
            
        else:
            context={'msg':'Invalid Email/Password'}
            return render(request,'landing/login.html',context)

    return render(request,'landing/login.html')

def Signup(request):
    if request.method=='POST':
        if signup.objects.filter(email_id=request.POST['email_id']):
            easygui.msgbox("This Emailid is already taken")
        else:
            if request.method=='POST':
                usignup=signup(name=request.POST['name'],
                               email_id=request.POST['email_id'],
                               password=request.POST['password']
                               )
                usignup.save()
                subject = 'Welcome to Enquete'
                message = "Hey there, \n\nThanks for signing up to keep in touch with Enquete.From now on, you'll get regular updates on surveys. \n \nCheers, \nEnquete"
                email_from = settings.EMAIL_HOST_USER
                recepient = request.POST.get('email_id')
                print("Check:",recepient)
                send_mail(subject,message,email_from,[recepient],fail_silently = False)
                easygui.msgbox("Registered Successfully!")
                return redirect(login)
    return render(request,'landing/login.html')

def survey(request):
    ut_data=signup.objects.get(name=multi_user_name)
    curr_id=signup.objects.get(id=user_current_id)
    var1=usercreatesurvey.objects.all()
    return render(request,'dashboard/user/survey.html',{'var1':var1,'ut_data':ut_data,'curr_id':curr_id})


def Create_survey(request):
    ut_data=signup.objects.get(name=multi_user_name)
    if request.method=='POST':
        usur_dis=usercreatesurvey(name=request.POST['name'],
                              number=request.POST['number']
                              )
        usur_dis.save()
        return redirect(survey)
    return render(request,'dashboard/user/survey.html',{'ut_data':ut_data})


def edit(request,id):
    ut_data=signup.objects.get(name=multi_user_name)
    curr_id=signup.objects.get(id=user_current_id)
    stu=usercreatesurvey.objects.get(id=id)
    return render(request,'dashboard/user/edit.html',{'stu':stu,'ut_data':ut_data,'curr_id':curr_id})


def editpage(request):
    ut_data=signup.objects.get(name=multi_user_name)
    return render(request,'dashboard/user/edit.html',{'ut_data':ut_data})

def Editu_survey(request,id):
    stu=usercreatesurvey(id=id,name=request.POST['name'],
                           number=request.POST['number']
                           )
     
    stu.save()
    return redirect(survey)


def deleteusersurvey(request,id):
    stu=usercreatesurvey.objects.get(id=id)
    stu.delete()
    return redirect(survey)
    

def Quest(request):
    ut_data=signup.objects.get(name=multi_user_name)
    if request.method=='POST':
        ask=uquest(email=request.POST['email'],
                   question=request.POST['question'],
                   )   
        ask.save()
        return redirect(survey)
    return render(request,'dashboard/user/edit.html',{'ut_data':ut_data})


def changepw(request,id):
    chan_pass=signup.objects.get(id=id)
    curr_pass=signup.objects.get(password=user_current_password)
    return render(request,'dashboard/user/changepw.html',{'chan_pass':chan_pass,'curr_pass':curr_pass})


def updatedpassword(request,id):
    curr_pass=signup.objects.get(password=user_current_password)
    if request.method == 'POST':
        oldpassword=request.POST['oldpassword']
        if oldpassword == curr_pass.password :
            update_pass=signup(id=id,name=request.POST['name'],
                               email_id=request.POST['email_id'],
                               password=request.POST['newpassword']
                               )
            update_pass.save()
            easygui.msgbox("Your password has been changed successfully!...")
            return redirect(login)
        else:
            easygui.msgbox("Incorrect Oldpassword redirected to Homepage")
            return redirect(survey)
    return redirect(survey)

def Uchp(request):
    if request.method=='POST':
        uchpassword=uchp(email=request.POST['email'],
                         oldpassword=request.POST['oldpassword'],
                         newpassword=request.POST['newpassword'],
                         confirmpassword=request.POST['confirmpassword']
                        )
        uchpassword.save()
        return redirect(login)
    return render(request,'landing/login.html')

def pay(request):
    ut_data=signup.objects.get(name=multi_user_name)
    curr_id=signup.objects.get(id=user_current_id)
    return render(request,'dashboard/user/pay.html',{'ut_data':ut_data,'curr_id':curr_id})

def adminlogin(request):
    if request.method=='POST':
        if adminsignup.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
            check=adminsignup.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
            global multi_admin_name
            global admin_current_password
            global admin_current_id
            multi_admin_name = check.name
            admin_current_password=check.password
            admin_current_id=check.id
            ad_data = adminsignup.objects.get(name=multi_admin_name)
            ad_curr_pass=adminsignup.objects.get(password=admin_current_password)
            ad_curr_id=adminsignup.objects.get(id=admin_current_id)
            easygui.msgbox("Loggedin successfully!!",title="ENQUETE")
            return redirect(home)
            # return render(request,'dashboard/admin/home.html')
        else:
            context={'msg':'Invalid Email/Password'}
            return render(request,'landing/adminlogin.html',context)

    return render(request,'landing/adminlogin.html')

def Asignup(request):
    if request.method=='POST':
        if adminsignup.objects.filter(email_id=request.POST['email_id']):
            easygui.msgbox("This Emailid is already taken")
        else:
            asignup=adminsignup(name=request.POST['name'],
                            email_id=request.POST['email_id'],
                            password=request.POST['password']
                            )
            asignup.save()
            subject = 'Welcome to Enquete'
            message = "Hi there, \n\nWe are delighted to have you among us. On behalf of all the members and the management, we would like to extend our warmest welcome and good wishes! \n\n\n\nCheers, \nEnquete"
            email_from = settings.EMAIL_HOST_USER
            recepient = request.POST.get('email_id')
            print("Check:",recepient)
            send_mail(subject,message,email_from,[recepient],fail_silently = False)
            easygui.msgbox("Registered Successfully!")
            return redirect(adminlogin)
    return render(request,'landing/adminlogin.html')

def home(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/home.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def dash(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/dash.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def userpage(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    user=signup.objects.all()
    return render(request,'dashboard/admin/userpage.html',{'user':user,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def edituserpage(request,id):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    user=signup.objects.get(id=id)
    return render(request,'dashboard/admin/edituserpage.html',{'user':user,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def Edituser(request,id):
    if request.method=='POST':
        user=signup(id=id,email_id=request.POST['email_id'],
                            name=request.POST['name'],
                            password=request.POST['password']
                        )
        user.save()
        return redirect(userpage)

def deleteuser(request,id):
    user=signup.objects.get(id=id)
    user.delete()
    return redirect(userpage)


def sur(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    survey=addsurvey.objects.all()
    return render(request,'dashboard/admin/sur.html',{'survey':survey,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def adminaddsurvey(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/addsurvey.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def Add_survey(request):
    if request.method=='POST':
        survey=addsurvey(email=request.POST['email'],
                         name=request.POST['surveyname'],
                         footer=request.POST['footer'],
                         effect=request.POST['effect'],
                        )
        survey.save()
        easygui.msgbox("Added Successfully!...")
        return redirect(sur)

def admineditsurvey(request,id):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    survey=addsurvey.objects.get(id=id)
    return render(request,'dashboard/admin/editsurvey.html',{'survey':survey,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def Editsurvey(request,id):
    if request.method=='POST':
        survey=addsurvey(id=id,email=request.POST['email'],
                               name=request.POST['surveyname'],
                               footer=request.POST['footer'],
                               effect=request.POST['effect'],
                               )
        survey.save()
        easygui.msgbox("Updated Successfully!...")
        return redirect(sur)

def deletesurvey(request,id):
    survey=addsurvey.objects.get(id=id)
    survey.delete()
    return redirect(sur)

def surq(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    quest=uquest.objects.all()
    return render(request,'dashboard/admin/surq.html',{'quest':quest,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def deletequestion(request,id):
    quest=uquest.objects.get(id=id)
    quest.delete()
    return redirect(surq)

def sura(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/sura.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def paym(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/paym.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def news(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/news.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def test(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    Testimonials= add_testimonials.objects.all()
    return render(request,'dashboard/admin/test.html',{'Testimonials':Testimonials,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def addtest(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    return render(request,'dashboard/admin/addtestimonial.html',{'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def addingtestimonial(request):
    if request.method == 'POST':
        Test = add_testimonials(name=request.POST['name'],
                                designation=request.POST['designation'],
                                status=request.POST['status']
                                )
        if len(request.FILES) !=0:
            Test.image = request.FILES['image']
        
        Test.save()
        easygui.msgbox("Added Successfully!...")
        return redirect(test)
    return render(request,'dashboard/admin/test.html')

def edittest(request,id):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    edit_test=add_testimonials.objects.get(id=id)
    return render(request,'dashboard/admin/edittest.html',{'edit_test':edit_test,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def Edittestimonials(request,id):
    if request.method=='POST':
        edit_test=add_testimonials(id=id,name=request.POST['name'],
                                         designation=request.POST['designation'],
                                         image=request.FILES['image'],
                                         status=request.POST['status']
                                          )
        edit_test.save()
        easygui.msgbox("Updated Successfully!...")
        return redirect(test)

def deletetestimonial(request,id):
    Test=add_testimonials.objects.get(id=id)
    Test.delete()
    return redirect(test)

def subs(request):
    ad_data = adminsignup.objects.get(name=multi_admin_name)
    ad_curr_id=adminsignup.objects.get(id=admin_current_id)
    subsc=subscriber.objects.all()
    return render(request,'dashboard/admin/subs.html',{'subsc':subsc,'ad_data':ad_data,'ad_curr_id':ad_curr_id})

def deletesubscriber(request,id):
    subsc=subscriber.objects.get(id=id)
    subsc.delete()
    return redirect(subs)

def chp(request,id):
    ad_chan_pass=adminsignup.objects.get(id=id)
    ad_curr_pass=adminsignup.objects.get(password=admin_current_password)
    return render(request,'dashboard/admin/chp.html',{'ad_chan_pass':ad_chan_pass,'ad_curr_pass':ad_curr_pass})

def adminupdatedpassword(request,id):
    ad_curr_pass=adminsignup.objects.get(password=admin_current_password)
    if request.method == 'POST':
        oldpassword=request.POST['oldpassword']
        if oldpassword == ad_curr_pass.password :
            ad_update_pass=adminsignup(id=id,name=request.POST['name'],
                                       email_id=request.POST['email_id'],
                                       password=request.POST['newpassword']
                                       )
            ad_update_pass.save()
            easygui.msgbox("password changed successfully!...")
            return redirect(adminlogin)
        else:
            easygui.msgbox("Incorrect Oldpassword redirected to Homepage")
            return redirect(home)
    return redirect(home)

def Achp(request):
    if request.method=='POST':
        adminchp=achp(oldpassword=request.POST['oldpassword'],
                      newpassword=request.POST['newpassword'],
                      confirmpassword=request.POST['confirmpassword']
                      )
        adminchp.save()
        return redirect(login) 
    return render(request,'landing/login.html')

def adminlogout (request):
    log(request)
    return render(request,'landing/adminlogin.html')

def userlogout(request):
    log1(request)
    return render(request,'landing/login.html')


