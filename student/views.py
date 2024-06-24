from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def stud(request):
    data={}
    if request.method == "POST":
        roll=request.POST.get('roll')
        data={
            'roll':roll
        }
        url=f"/result/{roll}/"
        print(url)
        return redirect(url)

    # p rint(data)
    return render(request,"student.html",data)
    # return HttpResponse(roll)
