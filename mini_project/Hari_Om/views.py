from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Volunteers
from .forms import volunteersForm
# Create your views here.


def index(request):
    contextdict = {
        "context_test": "this is coming from the context of views."}
    return render(request, "Hari_Om/index.html", context=contextdict)


def vol_form(request):

    form = volunteersForm(request.POST or None)
    if form.is_valid():
        res = form.save(commit=False)
        res.save()
        form.save_m2m()
        return redirect("table")

    else:
        form = volunteersForm()
    return render(request, "Hari_Om/register.html", {"form": form})


def display_table(request):
    obj = Volunteers.objects.all()

    return render(request, "Hari_Om/table.html", {"object": obj})
