from django.contrib import admin
<<<<<<< HEAD
from .models import TaskData
=======
from  taskData.models import TaskData


>>>>>>> 8b64436 (updated reset pssword method)

class TASKDATA(admin.ModelAdmin):
    disp_field = ("EmpID", "EmpName", "EmpEmail", "TaskName", "TaskStatus", "TaskSummary")
admin.site.register(TaskData, TASKDATA)
<<<<<<< HEAD
=======

>>>>>>> 8b64436 (updated reset pssword method)
# Register your models here.
