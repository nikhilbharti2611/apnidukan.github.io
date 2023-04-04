from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import urls
# from decimal import Decimal
from django.http import QueryDict
from myapp.models import additems
from myapp.models import register
from django.urls import reverse
import io



# Create your views here.
def index(request):
    return render(request, "index.html")

def List(request):
    return render(request, "List.html") 
def loginpage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pswd')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome, {uname}.")
            return redirect('List')
        else:
            return HttpResponse("<h3>Invalid Credentials. No such account found.<h3><h1> TRY AGAIN</h1>")
    return render(request, "login.html")

# page to display after the user LOGIN into the webiste

# logoutpage
def logoutpage(request):
    logout(request)
    return redirect('home')

def aboutus(request):
    return render(request, "aboutus.html")

def register(request):
    if request.method == "POST":
        uname = request.POST.get("user")
        email = request.POST.get("email")
        password = request.POST.get("pswd")
        # print(uname,email,password)
        register =  User.objects.create_user(uname,email,password)
        register.save()
        # return HttpResponse("Registered Successfully")
        messages.success(request, f'Registered Successfully!')
        return redirect('/login')
    return render(request, "register.html")

# saving form data to database
def savedata(request):
    # n = ''
    if request.method == 'POST':
        # selected_items = request.POST.getlist('item')
        input_box_value = request.POST.get('chkbox')
        amount = request.POST.get('priceinput')
        data3 = additems(itemname = input_box_value, amount = amount)
        data3.save()        
    return redirect('List')#,{'display_data':display_data})

# retrieving data from database
def displaydata(request):
    display_data = additems.objects.all()
    return render(request,'savedata.html',{'display_data':display_data})

# making QR code of a page
def makeQR(request):
    template_url  = reverse('myapp:savedata')
    return(request,template_url)

# def qr_code(request):
#     # Generate the QR code using the data from your template
#     qr = qrcode.QRCode(version=None, box_size=10, border=4)
#     qr.add_data(makeQR())  # Replace with data from your template
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")

#     # Write the QR code image to a byte stream
#     buffer = io.BytesIO()
#     img.save(buffer)
#     qr_image = buffer.getvalue()

#     # Return the QR code image as an HTTP response
#     return HttpResponse(qr_image, content_type="image/png")
