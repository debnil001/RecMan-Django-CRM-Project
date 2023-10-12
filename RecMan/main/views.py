from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    query=""
    students=Student.objects.all()
    if request.method == 'POST':
        if "add" in request.POST:
            name=request.POST.get("name")
            email=request.POST.get("email")
            Student.objects.create(
                name=name, 
                email=email
            )
            messages.success(request, "Student added successfully")
        
        elif "update" in request.POST:
            id=request.POST.get("id")
            name=request.POST.get("name")
            email=request.POST.get("email")

            student=Student.objects.get(id=id)
            student.name=name
            student.email=email
            student.save()
            messages.success(request,"Student updated successfully")
        
        elif "delete" in request.POST:
            id=request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request,"Student deleted successfully")
        elif "search" in request.POST:
            query=request.POST.get("searchquery")
            students=Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) )

    context={"students": students,"query": query}
    return render(request, 'index.html',context=context)
