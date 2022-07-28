
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from taskData import models
from django.contrib import messages
import taskData
from taskData.models import TaskData
import datetime



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
        taskStatus = (request.POST.get('option'))
        taskSummary = request.POST.get('tasksummary')
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(empId, empEmail, empName, taskName, dueDate, taskStatus, taskSummary)

        td = TaskData(empid=empId, empname=empName, empemail=empEmail, taskname=taskName.upper(), duedate=dueDate, taskstatus=taskStatus.title(), tasksummary=taskSummary+"      "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), createdon=cur_time)
        td.save()
        return redirect('home')

        # print(empId, empName, empEmail, taskName, dueDate, taskStatus, taskSummary)
        # print('successfull')
        # return HttpResponseRedirect('/')
    return render(request,"home-create-task.html")


#method to show completed and pending tasks and search
def search(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        empid = request.POST.get('empid')
        task = request.POST.get('task')
        print(fromdate, todate, empid, task)
        # searchData = TaskData.objects.raw(f"SELECT * FROM taskData_taskdata WHERE duedate BETWEEN '{fromdate}' AND '{todate}' AND empid={empid} AND taskname={task.upper()}")
        if fromdate =="" and todate =="":
            fromdate='1990-12-31'
            todate=datetime.datetime.now().strftime('%Y-%m-%d')
        searchData = TaskData.objects.filter(createdon__range=[fromdate, todate], empid__icontains=empid, taskname__icontains=task.upper())
        return render(request, "search.html", {"taskData":searchData})
    taskData = TaskData.objects.all().order_by('duedate')
    return render(request, "search.html", {"taskData":taskData})



@login_required(login_url="/login")
def updateTask(request, id):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080])"""
    getData = models.TaskData.objects.get(pk=id)
    # print(getData)
    if request.method == 'POST':
        getData = models.TaskData.objects.get(pk=id)
        getData.empname = request.POST.get('emp-name')
        getData.empemail = request.POST.get('emp-email')
        getData.taskname = request.POST.get('task-option').upper()
        getData.duedate = request.POST.get('due-date')
        getData.taskstatus = request.POST.get('task-status')
        getData.tasksummary = request.POST.get('task-summary')
        cur_time = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        getData.tasksummary = getData.tasksummary+"   <br>   "+cur_time
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
    
    return render(request, "hr-profile.html")

@login_required(login_url="/login")
def feedbackData(request):
    """Created by Sachin (ASE DATA ENGINEER) """
    
    return render(request, "feedback-rating-form.html")

# HR user registration 
def user_registration(request):
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
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            messages.info(request, "Invalid username or password...")
            return redirect('login')

    return render(request, 'login.html')

def resetPassword(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    return render(request, "password-reset.html")


def userLogout(request):
    """Created by Sachin PAl(ASE DATA ENGINEER[110080]) """
    logout(request)
    return redirect('login')

