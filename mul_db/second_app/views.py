from django.shortcuts import render
from second_app.models import Student_model
from second_app.forms import Student_create_form,Student_read_form
# Create your views here.


def createstudent(request):
    student_name=""
    Flag=False
    message=""
    student_id=""
    if(request.method=='POST'):
        form=Student_create_form(data=request.POST)
        if(form.is_valid()):
            form.save()
            student_id=request.POST['student_id']
            student_name=request.POST['student_name']
            Flag=True
            message="Succesfully Created"
        else:
            print('-------Student Data Not Saved--------')
            message="Not Succesfully"
    else:
        form=Student_create_form()
    return render(request,'second_app/createstudent.html',{"Flag":Flag,'form':form,'student_id':student_id,"student_name":student_name ,"message":message})


def readstudent(request):
    Flag=False
    student_name=""
    student_id=''
    message=""
    print('request.GET',request.GET)
    if(request.method=='GET'):
        student_id = request.GET.get('student_id', None)
        if(student_id is not None):
            form=Student_read_form(request.GET)
            
            print('---reademployee11-----')
            print("-----form.is_valid()------",form.is_valid())
            

            #employee_id=request.GET.get('employee_id')
            print('---reademployee-----')
            #employee_id = request.GET.get('employee_id', None)
            print('----employee_id----',student_id)
            query=Student_model.objects.get(student_id=student_id)
            employee_id=query.student_id
            student_name=query.student_name
            Flag=True
            print("--------",student_name,employee_id,"--------")
            message=" Succesfully Found"
        else:
                form=Student_read_form()
                message="NOT FOUND"
    
    else:
            form=Student_read_form()
            Flag=False
     
    return render(request,'second_app/readstudent.html',{"Flag":Flag,'form':form,'student_id':student_id,"student_name":student_name,"message":message})

