from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def sheet(request):
    return render(request,"sheet.html")



def result(request,roll):
    # if request.method == "POST":
    #     sl=request.POST['roll']

    details=markupdate.objects.filter(rollno=roll).values()[0]
    marks=[details['mark1'],details['mark2'],details['mark3'],details['mark4'],details['mark5'],details['mark6']]
    total=sum(marks)
    if marks[0] >=30 and marks[1] >=30 and marks[2] >=30 and marks[3] >=30 and marks[4] >=30 and marks[4] >=30 :
        status="PASS"
    else:
        status="FAIL"

    print(marks,total)
    per=(total/600)*100.
    per="{:.2f}".format(per)
    # print(sl)
    data={
        "details":details,
        'total':total,
        'result':status,
        'per':per
    }
    
    return render(request,'sheet.html',data)
    # return HttpResponse(mark6)