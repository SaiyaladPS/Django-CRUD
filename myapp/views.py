from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    return render(request, "about.html") 

def form(req):
    if req.method == "POST" :
        name = req.POST["name"]
        age = req.POST['age']

        person = Person.objects.create(
            name = name,
            age = age
        )
        person.save()
        messages.success(req, "Insert Success")
        return redirect("/")
    
    else :
        return render(req, "form.html") 
    
def edit(request, person_id) :
    if request.method == "POST" :
        person = Person.objects.get(id = person_id)
        person.name = request.POST['name']
        person.age = request.POST['age']
        person.save()
        messages.success(request, "Update Success")
        return redirect('/')
    else :
        person = Person.objects.get(id = person_id)
        return render(request, 'edit.html', {"person" : person})

def delete(request, person_id) :
    person = Person.objects.get(id = person_id)
    person.delete()
    messages.success(request, "Delete Success")
    return redirect('/')