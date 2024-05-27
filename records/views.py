from django.contrib import auth
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect
from employee.forms import LoginForm
from employee.models import Employee
from records.filters import RecordFilter
from records.forms import addRecord, addImage
from records.models import Record, Image
from django.urls import reverse
from datetime import date

def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            employee = auth.authenticate(username=username, password=password)

            if employee:
                auth.login(request, employee)
                return HttpResponseRedirect(reverse('employee:profile'))
    else:
        form = LoginForm()
        employee = Employee.objects.get(id=request.user.id)
        last_records = Record.objects.filter(visible=True).order_by("created_at")[:3]
        context = {
            'form': form,
            'employee': employee,
            'records': last_records
        }
    return render(request,'records/main.html', context)

def records(request):
    if request.method == 'POST':
        search = request.POST.get('search', False)
        localisation = request.POST.get('localisation', False)
        date_from = request.POST.get('from', False)
        date_to = request.POST.get('to', False)
        deleted = request.POST.get('deleted', False)

        author_id = Employee.objects.filter(fullname__icontains=search)

        q_fullname = Q(fullname__icontains=search) if search else Q()
        q_desc = Q(description__icontains=search) if search else Q()
        q_author = Q(author=author_id[0].id) if search and author_id.count() > 0 else Q()
        q_localisation = Q(localisation=localisation) if localisation else Q()
        q_date = Q(created_at__range=(date_from, date_to)) if date_from and date_to else Q(created_at__range=('1900-01-01', '2099-01-01'))

        if deleted:
            records = Record.objects.filter(q_date, q_localisation, q_fullname | q_desc | q_author, visible=False)
        else:
            records = Record.objects.filter(q_date, q_localisation, q_fullname | q_desc | q_author, visible=True)

        # records = Record.objects.filter(q_date, q_localisation, q_fullname | q_desc | q_author, visible=)

        context = {'records': records}

        return render(request, 'records/records.html', context)
    else:
        records = Record.objects.filter(visible=True)
        employees = Employee.objects.all().prefetch_related('author')
        employee = Employee.objects.get(id=request.user.id)
        context = {
            'records': records,
            'employees': employees,
            'employee': employee
        }
        return render(request, 'records/records.html', context)

def id(request, id):
    record = Record.objects.get(id=id)
    images = Image.objects.filter(record_id=id)
    employee = Employee.objects.get(id=record.author)
    editForm = addRecord(request.POST or None, instance=record)
    files = request.FILES.getlist("image")
    ids = request.POST.getlist('id_for_delete')

    if editForm.is_valid():
        for t in ids:
            Image.objects.get(id=t).delete()

        f = editForm.save()
        f.save()
        print(f)
        for i in files:
            Image.objects.create(record=f, image=i)

        return HttpResponseRedirect(reverse('record:records'))
    else:
        print(editForm.errors)

    context = {
        'record': record,
        'editForm': editForm,
        'images': images,
        'employee': employee
    }
    return render(request, 'records/record_edit.html', context)

def analytics(request):
    if request.method == 'POST':

        from_date = request.POST['from']
        to_date = request.POST['to']
        records = Record.objects.filter(created_at__range=[from_date, to_date])

        context = {
            'records': records
        }
        return render(request, 'records/analytics.html', context)
    else:
        current_date = date.today()
        last_date = current_date - date.timedelta(days=30)
        records = Record.objects.filter(created_at__range=[current_date, last_date])

        context = {
            'records': records
        }
        return render(request, 'records/analytics.html', context)