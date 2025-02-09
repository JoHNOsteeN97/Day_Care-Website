from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from myproject import settings  
from django.core.mail import send_mail  
# Create your views here.
def home (request):
    return render(request,'home.html')

def aboutus (request):
    return render(request,'aboutus.html')

def gallery (request):
    return render(request,'gallery.html')

def contactus (request):
    if request.method=="POST":
        name=request.POST['ename']
        email=request.POST['email']
        message=request.POST['msg']
        Message.objects.create(ename=name,email=email,msg=message,type=0)
        subject = "Welcome to tiny treasures"  
        msg     = """Thank you for using our feedback service.
        Our executive will contact you as soon as possible.
        """  
        to      = email 
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        return redirect(home)
    else:
        return render(request,'contactus.html')

def Parents (request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        ph_number=request.POST['ph_number']
        place=request.POST['place']
        address=request.POST['address']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        id_proof=request.POST['idproof']
        occupation=request.POST['occupation']
        User.objects.create_user(first_name=first_name,last_name=last_name,ph_number=ph_number,place=place,address=address,email=email,username=username,password=password,id_proof=id_proof,occupation=occupation,usertype=1)
        return redirect(home)
    else:
        return render(request,'preg.html')
    
def handle_uploaded_file(f):  
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
             
def Caretaker (request):
    try:
        if request.method == 'POST':
            first=request.POST['fname']
            last=request.POST['lname']
            ph_number=request.POST['ph_number']
            place=request.POST['place']
            addres=request.POST['address']
            mail=request.POST['email']
            qualification=request.POST['qualification']
            dob=request.POST['dob']
            username=request.POST['username']
            password=request.POST['password']
            resume=request.FILES['res']
            handle_uploaded_file(resume)
            User.objects.create_user(first_name=first,last_name=last,ph_number=ph_number,place=place,address=addres,email=mail,qualification=qualification,dob=dob,resume=resume,username=username,password=password,usertype=2,caretaker_status=0)
            return redirect(home)
        else:
            return render(request,'creg.html')
    except:
        return redirect(Caretaker)
    
def Logins (request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None and user.usertype==1:
            request.session['pid']=user.id
            login(request,user)
            return redirect(pdash)
        elif user is not None and user.usertype==2 and user.caretaker_status==1:
            request.session['cid']=user.id
            login(request,user)
            return redirect(caredash)
        
        elif user is not None and user.is_superuser==1:
            request.session['aid']=user.id
            login(request,user)
            return redirect(adash)
        else:
            return render(request,'login.html',{'msg':'Incorrect Credentials'})
            
    else:
        return render(request,'login.html')

    def lgout(request):
        logout(request) 
        return redirect(Logins)
    
def pdash (request):
    id=request.session['pid']
    data=User.objects.filter(id=id).get()
    return render(request,'prntdes.html',{'data':data})




def children (request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        age=request.POST['age']
        blood_group=request.POST['blood_group']
        medical_condition=request.POST['medical_condition']
        Children.objects.create(fname=first_name,lname=last_name,age=age,parent_id=request.session['pid'],blood_group=blood_group,medical_condition=medical_condition)
        return redirect(pdash)
    else:
        data=list(range(1,9))
        return render(request,'childreg.html',{'data':data})
    
    
def pedit(request):
    if request.method=='POST':
        id=request.session['pid']
        
        ph_number=request.POST['ph_number']
        address=request.POST['address']
        email=request.POST['email']
        User.objects.filter(id=id).update(ph_number=ph_number,address=address,email=email)
        return redirect (pdash)
    else:
        id=request.session['pid']
        data=User.objects.filter(id=id).get()
        return render(request,'pedit.html',{'data':data})    

def emergency(request):
    if request.method=="POST":
        name=request.POST['ename']
        email=request.POST['email']
        message=request.POST['msg']
        Message.objects.create(ename=name,email=email,msg=message,type=1)
        subject = "Welcome to tiny treasures"  
        msg     = """Thank you for using our feedback service.
        Our executive will contact you as soon as possible.
        """  
        to      = email 
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        return redirect(pdash)
    else:
        id=request.session['pid']
        data=User.objects.filter(id=id).get()
        return render(request,'emergency.html',{'data':data})
        
        
def pviewchild(request):
    id=request.session['pid']
    data=Children.objects.filter(parent_id=id).all()
    return render(request,'pviewchild.html',{'data':data})
       

def childedit(request,id):
    if request.method=='POST':
        age=request.POST['age']
        mc=request.POST['mc']
        Children.objects.filter(id=id).update(age=age,medical_condition=mc)
        return redirect (pviewchild)
    else:
        data=Children.objects.filter(id=id).get()
        return render(request,'childedit.html',{"data":data})
             

def pbookappoint(request):
    if request.method=='POST':
        date=request.POST['date']
        child=request.POST['schild']
        Appointment.objects.create(date_app=date,child_id=child)
        return redirect (pdash)
        
    else:
        id=request.session['pid']
        data=Children.objects.filter(parent_id=id).all()
        return render(request,'bookappoint.html',{'data':data})
    
def adash (request):
    id=request.session['aid']
    data=User.objects.filter(id=id).get()
    return render(request,'addes.html',{'data':data})


def adedit(request):
    if request.method=='POST':
        id=request.session['aid']
        
        ph_number=request.POST['ph_number']
        address=request.POST['address']
        email=request.POST['email']
        User.objects.filter(id=id).update(ph_number=ph_number,address=address,email=email)
        return redirect (adash)
    else:
        id=request.session['aid']
        data=User.objects.filter(id=id).get()
        return render(request,'adedit.html',{'data':data}) 
    
def showmsg(request):
    data=Message.objects.filter(type=0).all()
    return render(request,'showmsg.html',{'data':data})

def delmsg(request,id):
    Message.objects.filter(id=id).delete()
    return redirect(showmsg)
        

def adminviewappoint(request):
    data=Appointment.objects.filter(app_status=0).all()
    return render(request,'showappoint.html',{'data':data})      
        
def adviewchild(request,id):
    data=Children.objects.filter(id=id).get()
    return render(request,'adviewchild.html',{'data':data})


def approveappt(request,id):
    Appointment.objects.filter(id=id).update(app_status=1)
    return redirect(adminviewappoint)

def rejectappt(request,id):
    Appointment.objects.filter(id=id).delete()
    return redirect(adminviewappoint)


def recruitment(request):
    data=User.objects.filter(usertype=2,caretaker_status=0).all()
    for i in data:
        print(i.resume)
    return render(request,'recruitmemt.html',{'data':data})
    
def approvecr(request,id):
    User.objects.filter(id=id).update(caretaker_status=1)
    data=User.objects.filter(id=id).get()
    subject = "Approval From Manager"  
    msg     = """Your resume has been Shortlisted.
    Kindly log in to your profile for more after first office visit.
        """  
    to      = data.email 
    send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    return redirect(recruitment)

def rejectcr(request,id):
    User.objects.filter(id=id).delete()
    return redirect(recruitment)


def adminviewcr(request):
    data=User.objects.filter(caretaker_status=1,usertype=2).all()
    return render(request,'showapprovecr.html',{'data':data})   




def credit(request,id):
    if request.method=='POST':
        salary=request.POST['salary']
        User.objects.filter(id=id).update(salary=salary)
        return redirect (adminviewcr)
    else:
        data=User.objects.filter(id=id).get()
        return render(request,'credit.html',{"data":data})   
        
def crdelete(request,id):
    User.objects.filter(id=id).delete()
    return redirect(adminviewcr)
    
def allotcr(request):
    if request.method=='POST':
        alot=request.POST['alot']
        ch=request.POST['ch']
        ch_data=Children.objects.filter(id=ch).update(caretaker_id=alot)
        return redirect(allotcr)
    else:
        cr_data=User.objects.filter(caretaker_status=1).all()
        ch_data=Children.objects.filter(caretaker_id=0).all()
        return render(request,'allotcr.html',{'cr_data':cr_data,'ch_data':ch_data})
        
def caredash(request):
    id=request.session['cid']
    data=User.objects.filter(id=id).get()
    return render(request,'caretakdes.html',{'data':data})

def emrmsg(request):
    data=Message.objects.filter(type=1).all()
    return render(request,'showemergency.html',{'data':data})

def delemr(request,id):
    Message.objects.filter(id=id).delete()
    return redirect(caredash)

def crviewchild(request):
    id=request.session['cid']
    data=Children.objects.filter(caretaker_id=id).all()
    return render(request,'crviewchild.html',{'data':data})

def sendreply(request,email):
    if request.method == 'POST':
        msg=request.POST['msg']
        subject = "Replay for your Query"  

        to      = email 
        send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
        return redirect(emrmsg)
        
    else:
        return render(request,'sendreply.html')
    
    
    
    
def cedit(request):
    if request.method=='POST':
        id=request.session['cid']
        
        ph_number=request.POST['ph_number']
        address=request.POST['address']
        email=request.POST['email']
        User.objects.filter(id=id).update(ph_number=ph_number,address=address,email=email)
        return redirect (caredash)
    else:
        id=request.session['cid']
        data=User.objects.filter(id=id).get()
        return render(request,'caretakeedit.html',{'data':data})    
    
    

    
    