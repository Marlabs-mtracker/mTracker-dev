
from calendar import c
<<<<<<< HEAD
from getpass import getuser
=======
>>>>>>> 8b64436 (updated reset pssword method)
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from matplotlib.ft2font import LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH
# from django.contrib.auth.models import User
from accounts.models import User
from taskData import models
from django.contrib import messages
import taskData
from taskData.models import TaskData
import datetime
import re
=======
from django.contrib.auth.models import User
from taskData import models
from django.contrib import messages
from taskData.models import TaskData
from userProfile.models import *
import uuid 
import datetime
import re
from django.core.mail import send_mail
from django.conf import settings

>>>>>>> 8b64436 (updated reset pssword method)



#creating tasks
@login_required(login_url="/login")
def home(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.method == "POST":
        empId = request.POST.get('empid')
        empName = request.POST.get('empname')
        empEmail = request.POST.get('empemail')
        taskName = request.POST.get('task-option')
        dueDate = request.POST.get('date')
        taskStatus = (request.POST.get('option')).title()
        taskSummary = request.POST.get('tasksummary')
        cur_time = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
<<<<<<< HEAD
        # print(empId, empEmail, empName, taskName, dueDate, taskStatus, taskSummary)
=======
        print(empId, empEmail, empName, taskName, dueDate, taskStatus, taskSummary)
>>>>>>> 8b64436 (updated reset pssword method)

        td = TaskData(empid=empId, empname=empName, empemail=empEmail, taskname=taskName, duedate=dueDate, taskstatus=taskStatus, tasksummary=taskSummary+"      "+cur_time)
        check_id = re.findall('[0-9]',empId)
        if len(empId) < 6:
            messages.error(request, "EmpID should be 6 to 8 digit ")
            return redirect('home')
        elif len(empId) >= 8:
            messages.error(request, "EmpID should be 6 to 8 digit ")
            return redirect('home')
        elif not check_id:
            messages.error(request, "EmpId should be in digit")
            return redirect('home')
        else:
            td.save()
            return redirect('home')

        # print(empId, empName, empEmail, taskName, dueDate, taskStatus, taskSummary)
        # print('successfull')
        # return HttpResponseRedirect('/')
    return render(request,"home-create-task.html")


#method to show completed and pending tasks and search
<<<<<<< HEAD
=======
@login_required(login_url="/login") 
>>>>>>> 8b64436 (updated reset pssword method)
def search(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    taskData = TaskData.objects.all()
    return render(request, "search.html", {"taskData":taskData})

<<<<<<< HEAD

#Only show result with Pending Task with a specific empid
=======
#Only show result with Pending Task with a specific empid
@login_required(login_url="/login")
>>>>>>> 8b64436 (updated reset pssword method)
def searchResult(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    
    if request.method == "POST":
        searchData = request.POST.get("search")
<<<<<<< HEAD
        finalData = TaskData.objects.filter(empid=searchData)
=======
        finalData = TaskData.objects.filter(empid=searchData).exclude(taskstatus="Completed")
>>>>>>> 8b64436 (updated reset pssword method)
    return render(request, "searchresult.html",{"finalData":finalData})

@login_required(login_url="/login")
def updateTask(request, id):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    getData = models.TaskData.objects.get(pk=id)
    # print(getData)
    if request.method == 'POST':
        getData = models.TaskData.objects.get(pk=id)
        getData.empname = request.POST.get('emp-name')
        getData.empemail = request.POST.get('emp-email')
        getData.taskname = request.POST.get('task-option')
        getData.duedate = request.POST.get('due-date')
        getData.taskstatus = request.POST.get('task-status')
        getData.tasksummary = request.POST.get('task-summary')
        cur_time = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        getData.tasksummary = getData.tasksummary+"      "+cur_time
        getData.save()
        # print(getData.empname)
        messages.success(request, 'You successfully updated your data!')
        return redirect('search')

    return render(request, "updatetask.html", {'getData':getData})

@login_required(login_url="/login")
def deleteTask(request, id):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.method == "POST":
        getData = models.TaskData.objects.get(pk=id)
        # print(getDeletedData)
<<<<<<< HEAD
        getData.delete()
=======
        print(getData.delete())
>>>>>>> 8b64436 (updated reset pssword method)
        # messages.success(request, 'You successfully deleted')
        return redirect('search')
    return HttpResponse('404 no page found!')
    # return render(request, "search.html", {"getData":getData})


@login_required(login_url="/login")
def profileData(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
<<<<<<< HEAD
    totalTasks = TaskData.objects.all().count()
    totalTasksCompleted = TaskData.objects.filter(taskstatus="Completed").count()
    tottalTasksPending = TaskData.objects.filter(taskstatus="Pending").count()
    # print(totalTasks, totalTasksCompleted, tottalTasksPending)
    context = {      
        "totalTasks":totalTasks,
        "totalTasksCompleted":totalTasksCompleted,
        "totalTasksPending":tottalTasksPending
    }
    return render(request, "hr-profile.html",context=context)
=======
    return render(request, "hr-profile.html")
>>>>>>> 8b64436 (updated reset pssword method)

@login_required(login_url="/login")
def feedbackData(request):
    """Created by Sachin (ASE DATA ENGINEER) """
<<<<<<< HEAD
    
=======
>>>>>>> 8b64436 (updated reset pssword method)
    return render(request, "feedback-rating-form.html")

# HR user registration 
def user_registration(request):
<<<<<<< HEAD
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        empid = request.POST.get('employeeid')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        location = request.POST.get('location')
        password = request.POST.get('password')
        conf_emp_password = request.POST.get('conf_password')

        # print(first_name, empid, email, password, conf_emp_password, designation, location)

        if password == conf_emp_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Employee email already registered...")
                return redirect(user_registration)
            else:
                user = User.objects.create_user(email=email, password=password, empid=empid, first_name=first_name, last_name=last_name, designation=designation, location=location)
                user.save()
=======
    """Created by Sachin PAl(ASE DATA ENGINEER[110080] And Ashish Upadhyay [110070])"""
    if request.method == 'POST':
        first_name = request.POST.get('name')
        username = request.POST.get('employeeid')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_emp_password = request.POST.get('conf_password')

        print(first_name, username, email, password, conf_emp_password)

        if password == conf_emp_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Employee Id already registered..")
                return redirect(user_registration)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Employee email already registered...")
                return redirect(user_registration)
            else:
                user_obj = User.objects.create_user(username=username, password=password, email=email, first_name=first_name)
                user_obj.set_password(password)
                user_obj.save()
                ftoken = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj,forget_password_token=ftoken)
                profile_obj.save()
                subject = 'About registration on mTracker'
                message = f'Hi {first_name}, You has been registerd successfully on mTracker'
                email_from = settings.EMAIL_HOST_USER
                receipent_list = [email,]
                send_mail(subject, message, email_from,receipent_list)
                messages.success(request,'User has been registerd successfully')
>>>>>>> 8b64436 (updated reset pssword method)
                return redirect('login')
        else:
            messages.info(request, "Both password are not matching...")
            return redirect(user_registration)
    return render(request, 'register.html')

#HR user login
def userLogin(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
<<<<<<< HEAD
    if request.user.is_authenticated:
        return redirect('search')

=======
>>>>>>> 8b64436 (updated reset pssword method)
    if request.method == "POST":
        username = request.POST.get('emp-id')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(username=username, password=password)
<<<<<<< HEAD
        # print(user)
=======
        print(user)
>>>>>>> 8b64436 (updated reset pssword method)
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            messages.info(request, "Invalid username or password...")
            return redirect('login')

    return render(request, 'login.html')

<<<<<<< HEAD
def resetPassword(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    password = User.password()
    print(password)
    return render(request, "password-reset.html")
=======
>>>>>>> 8b64436 (updated reset pssword method)


def userLogout(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    logout(request)
    return redirect('login')

<<<<<<< HEAD
=======

def resetPassword(request):
    """Created by Ashish Upadhyay(ASE DATA ENGINEER[110070]) """
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/password-reset/')
            
            user = User.objects.get(username = username)
            user_mail = user.email
            profile= Profile.objects.get(user = user)
            ftoken = profile.forget_password_token
            mail_message = f'Hey your reset password link is http://127.0.0.1:8000/changepass/{ftoken}/'
            send_mail('Password Reset Request',mail_message,settings.EMAIL_HOST_USER,[user_mail])
            messages.success(request, 'An email is sent.')
            return redirect('/password-reset/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'password-reset.html')


def changePassword(request,id):
    """Created by Ashish Upadhyay(ASE DATA ENGINEER[110070]) """
    if request.method == 'POST':
        password = request.POST['password']
        profile = Profile.objects.get(forget_password_token=id).user
        user = User.objects.get(username = profile)
        user.set_password(password)
        user.save()
        messages.success(request,'Password Successfully Changed Please Login')
        return redirect('login')
    return render(request,'changepassword.html')
>>>>>>> 8b64436 (updated reset pssword method)
