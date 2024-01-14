from django.shortcuts import render
from first_app.models import employee_model
from first_app.forms import Employee_create_form,Employee_read_form
# Create your views here.


def index(request):
    return render(request,'first_app/index.html')


def createmployee(request):
    employee_name=""
    Flag=False
    message=""
    employee_id=""
    if(request.method=='POST'):
        form=Employee_create_form(data=request.POST)
        if(form.is_valid()):
            form.save()
            employee_id=request.POST['employee_id']
            employee_name=request.POST['employee_name']
            Flag=True
            message="Succesfully Created"
        else:
            print('-------Employee Data Not Saved--------')
            message="Not Succesfully"
    else:
        form=Employee_create_form()
    return render(request,'first_app/createemployee.html',{"Flag":Flag,'form':form,'employee_id':employee_id,"employee_name":employee_name ,"message":message})


def reademployee(request):
    Flag=False
    employee_name=""
    employee_id=''
    message=""
    print('request.GET',request.GET)
    if(request.method=='GET'):
        employee_id = request.GET.get('employee_id', None)
        if(employee_id is not None):
            form=Employee_read_form(request.GET)
            
            print('---reademployee11-----')
            print("-----form.is_valid()------",form.is_valid())
            

            #employee_id=request.GET.get('employee_id')
            print('---reademployee-----')
            #employee_id = request.GET.get('employee_id', None)
            print('----employee_id----',employee_id)
            query=employee_model.objects.get(employee_id=employee_id)
            employee_id=query.employee_id
            employee_name=query.employee_name
            Flag=True
            print("--------",employee_name,employee_id,"--------")
            message=" Succesfully Found"
        else:
                form=Employee_read_form()
                message="NOT FOUND"
    
    else:
            form=Employee_read_form()
            Flag=False
     
    return render(request,'first_app/reademployee.html',{"Flag":Flag,'form':form,'employee_id':employee_id,"employee_name":employee_name,"message":message})

