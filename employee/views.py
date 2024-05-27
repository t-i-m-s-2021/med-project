from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from employee.models import Employee
from employee.forms import RegisterForm
from django.urls import reverse
from records.forms import addRecord, addImage
from records.models import Record, Image

def profile(request):
    if request.method == 'POST':
        record = addRecord(request.POST)
        files = request.FILES.getlist("image")

        if record.is_valid():
            f = record.save(commit=False)
            f.author = request.user.id
            f.visible = True
            f.save()
            print(f)
            for i in files:
                Image.objects.create(record=f, image=i)

            return HttpResponseRedirect(reverse('employee:profile'))
        else:
            print(record.errors)

    else:
        form = Employee.objects.get(id=request.user.id)
        add = RegisterForm
        image = addImage
        record = addRecord
        my_records = Record.objects.filter(author=request.user.id)

        context = {
            'form': form,
            'add': add,
            'record': record,
            'image': image,
            'my_records': my_records
        }
        return render(request, 'employee/profile.html', context)

def user(request, id):
    employee = Employee.objects.get(id=id)

    print(employee)
    records = Record.objects.filter(author=id)

    context = {
        'employee': employee,
        'records': records
    }
    return render(request, 'employee/user.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
