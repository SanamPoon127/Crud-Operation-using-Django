from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistation
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistation(request.POST)
        if fm.is_valid():
            #fm.save()# This saves form data to the database (User table)
            # If you want to manually process the form data, you can do something like this:
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']  # If you don't want to process or use this data, you can remove it.
            pw = fm.cleaned_data['password']  # This is for manually saving form data into the User table
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistation()  # this resets the form after adding student data
            
    else:
        fm = StudentRegistation()  # Creates an empty form
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# Function to Update/Edit User Data
def update_data(request, id):
    pi = User.objects.get(pk=id)
    if request.method == 'POST':
        fm = StudentRegistation(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')  # Redirect to home or another relevant page
    else:
        fm = StudentRegistation(instance=pi)  # Pre-fill the form with existing data

    return render(request, 'enroll/updatestudent.html', {'form': fm})

#This function will delete data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') #this code will send to home page
