from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    e_list = Event.objects.all()
    e_list.exclude(id=5)
    s_list = Student.objects.all()
    count = 0
    for s in s_list:
        count += s.stud_part_events.event_fee

    return render(request, 'fest_app/home.html', {"e_list": e_list, 'total': count})


def register(request, id, *args, **kwargs):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.stud_part_events = Event.objects.get(id=id)
        obj.save()
        return redirect('home')
    else:
        form = StudentForm()

    return render(request, 'fest_app/stud_register.html', {'id': id, 'form': form})


@login_required(login_url='/accounts/login/')
def CreateEvent(request):

    form1 = EventForm(request.POST or None)

    # print(form1['event_date_time_field'].value())

    if form1.is_valid():
        obj = form1.save(commit=False)
        #obj.event_date_time = form1['event_date_time_field'].value()

        obj.save()
        return redirect('home')
    else:
        form1 = EventForm()
    return render(request, 'fest_app/create_event.html', {'form': form1})


def CreateJury(request):
    form2 = JuryForm(request.POST or None)
    if form2.is_valid():
        obj = form2.save(commit=False)
        obj.save()
        return redirect('jury')
    else:
        form2 = JuryForm()
    return render(request, 'fest_app/jury_form.html', {
        'form': form2})


def Update(request, id, *args, **kwargs):
    obj = get_object_or_404(Event, id=id)

    form = EventForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'fest_app/updateform.html', {'form': form})


def DeleteEvent(request, id, *args, **kwargs):

    obj = Event.objects.get(id=id)
    obj.delete()
    return redirect('home')


@login_required(login_url='/accounts/login/')
def Visitor(request, id, *args, **kwargs):
    queryset = Student.objects.filter(stud_part_events=id)
    total = len(queryset)*Event.objects.get(id=id).event_fee
    return render(request, 'fest_app/visitor.html', {'id': id, 'studentlist': queryset, 'fee': total})
