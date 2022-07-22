
from calendar import c
from getpass import getuser
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from taskData import models
from django.contrib import messages
import taskData
from taskData.models import TaskData
import datetime
import re



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
        # print(empId, empEmail, empName, taskName, dueDate, taskStatus, taskSummary)

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
def search(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    taskData = TaskData.objects.all()
    return render(request, "search.html", {"taskData":taskData})


#Only show result with Pending Task with a specific empid
def searchResult(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    
    if request.method == "POST":
        searchData = request.POST.get("search")
        finalData = TaskData.objects.filter(empid=searchData).exclude(taskstatus="Completed")
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
        getData.delete()
        # messages.success(request, 'You successfully deleted')
        return redirect('search')
    return HttpResponse('404 no page found!')
    # return render(request, "search.html", {"getData":getData})


@login_required(login_url="/login")
def profileData(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    userData = User.objects.get(username=request.user)
    print(userData.first_name)
    totalTasks = TaskData.objects.all().count()
    totalTasksCompleted = TaskData.objects.filter(taskstatus="Completed").count()
    tottalTasksPending = TaskData.objects.filter(taskstatus="Pending").count()
    # print(totalTasks, totalTasksCompleted, tottalTasksPending)
    context = {
        "userData":userData,
        "totalTasks":totalTasks,
        "totalTasksCompleted":totalTasksCompleted,
        "totalTasksPending":tottalTasksPending
    }
    return render(request, "hr-profile.html",context=context)

@login_required(login_url="/login")
def feedbackData(request):
    """Created by Sachin (ASE DATA ENGINEER) """
    return render(request, "feedback-rating-form.html")

# HR user registration 
def user_registration(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    
    if request.method == 'POST':
        first_name = request.POST.get('name')
        username = request.POST.get('employeeid')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_emp_password = request.POST.get('conf_password')

        # print(first_name, username, email, password, conf_emp_password)

        if password == conf_emp_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Employee Id already registered..")
                return redirect(user_registration)
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Employee email already registered...")
                return redirect(user_registration)
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Both password are not matching...")
            return redirect(user_registration)
    return render(request, 'register.html')

#HR user login
def userLogin(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    if request.user.is_authenticated:
        return redirect('search')

    if request.method == "POST":
        username = request.POST.get('emp-id')
        password = request.POST.get('password')

        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            messages.info(request, "Invalid username or password...")
            return redirect('login')

    return render(request, 'login.html')

def resetPassword(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    password = User.password()
    print(password)
    return render(request, "password-reset.html")


def userLogout(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    logout(request)
    return redirect('login')

