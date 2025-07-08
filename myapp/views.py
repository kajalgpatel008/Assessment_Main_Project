from django.shortcuts import render,redirect
from .models import AboutImage,AboutGalleryImage,Speaker,Schedule,Blog,Contact,Event,TicketBook,User
import requests
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    images = AboutImage.objects.all() 
    gallery_images= AboutGalleryImage.objects.all()  
    return render(request,'about.html', {'images': images, 'gallery_images': gallery_images})

def speakers(request):
    speakers = Speaker.objects.all()
    return render(request,'speakers.html', {'speakers': speakers})

def schedule(request):
    return render(request,'schedule.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html', {'blogs': blogs})

def contact(request):
    return render(request,'contact.html')

def event(request):
    events = Event.objects.all()
    return render(request, 'event.html', {'events': events})

def ticket_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        event = request.POST['event']
        date = request.POST['date']

        request.session['booking_data']={
            'name': name,
            'email': email,
            'event':event,
            'date': date
        }
        msg="Ticket Booking successfully"
        return redirect('ticket-success')
    else:
        msg = "Please fill all fields correctly."
        return render(request, 'ticket-form.html', {'msg': msg})

def ticket_success(request):
    return render(request, 'ticket-success.html')

def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request, 'signup.html', {'msg': msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture'],     
                )
                msg="User Created Successfully"
                return render(request, 'signup.html', {'msg': msg})
            else:
                msg="Password and Confirm Password do not match"
                return render(request, 'signup.html', {'msg': msg})
    else:
        return render(request,'signup.html')   
    return render(request, 'signup.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_picture']=user.profile_picture.url
                return render(request,'index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg': msg})
        except:
            msg="Email Not Registered" 
            return render(request, 'login.html',{'msg': msg})
    else:
        return render(request, 'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['profile_picture']   
        del request.session['fname']
    except:
        pass
    return render(request,'login.html') 

def change_password(request):
    if request.method == "POST":
        user=User.objects.get(email=request.session['email'])
        if user.password == request.POST['old_password']:
            if request.POST['new_password'] == request.POST['cnew_password']:
                if user.password != request.POST['new_password']:
                    user.password = request.POST['new_password']
                    user.save()
                    del request.session['email']
                    del request.session['fname']
                    del request.session['user_image']
                    msg="Password Changed Successfully"
                    return render(request,'login.html',{'msg':msg})
                else:
                    msg="Your New Password cannot be from Your Old Password"
                    return render(request,'change-password.html',{'msg':msg})
            else:
                msg="New Password and Confirm New Password do not match"
                return render(request,'change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched"
            return render(request,'change-password.html',{'msg':msg})
    else:
        return render(request,'change-password.html')

def forgot_password(request):
    if request.method=="POST":
        try:
            API_Key= "6cb93bef-41fb-11f0-a562-0200cd936042"
            user=User.objects.get(mobile=request.POST['mobile'])
            otp=random.randint(1000,9999)
            print(otp)
            url = f"https://2factor.in/API/V1/{API_Key}/SMS/{int(user.mobile)}/{otp}/Your OTP is"
            payload={}
            headers ={'content-type': 'application/x-www-form-urlencoded'}
            response= requests.get(url, data=payload ,headers=headers)
            print(response)
            request.session['otp']=otp
            request.session['mobile']=user.mobile
            return render(request,'otp.html')
        except:
            msg="Mobile Number Not Registered"
            return render(request,'forgot-password.html',{'msg': msg})
    else:
        return render(request, 'forgot-password.html')

def verify_otp(request):
    if int(request.POST['otp']) == request.session['otp']:
        del request.session['otp']
        return render(request,'new-password.html')
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'msg':msg})

def new_password(request):
    if request.POST['new_password'] == request.POST['cnew_password']:
        user=User.objects.get(email=request.session['e'])
        user.password = request.POST['new_password']
        user.save()
        del request.session['e']
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New Password and Confirm New Password do not matched"
        return render(request,'new-password.html',{'msg':msg})







