from django.shortcuts import render,redirect
from .models import Employee
from .forms import UpdateEmployeeForm
# Create your views here.
#home
def home(request):
    data=Employee.objects.filter(IsDelete=False)
    
    context =  {'data':data}    
    return render(request,"index.html",context)

# Add View
def add(request):
    
    form = UpdateEmployeeForm
    
    if request.method == "POST":
          form = UpdateEmployeeForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')
    context = {'form':form}
    return render(request,"add.html",context)
    

def update(request,pk):
    data = Employee.objects.get(id=pk)
    
    form = UpdateEmployeeForm(instance=data)
    if request.method == "POST":
        form = UpdateEmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form} 
    return render(request,"update.html",context)



def delete(request,pk):
    employee=Employee.objects.get(id=pk)
    employee.IsDelete=True
    employee.save()
    return redirect('home')

# Git changes