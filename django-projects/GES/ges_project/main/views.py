from django.shortcuts import render
from main.models import Course,Prize,Information,Filial,Vacancy,Staff,Register
from django.http.response import JsonResponse

def IndexHandler(request):
    if request.method == 'GET':
        information = None
        courses = Course.objects.filter(status=0).order_by('-rating')
        prizes = Prize.objects.filter(status=0).order_by('-rating')
        informations = Information.objects.filter(status=0)
        if informations:
            information = informations[0]
        filials = Filial.objects.filter(status=0).order_by('-rating')
        vakancies = Vacancy.objects.filter(status=0).order_by('-rating')
        staffs = Staff.objects.filter(status=0).order_by('-rating')



        return render(request,'base.html',{
            'courses':courses,
            'prizes':prizes,
            'information':information,
            'filials':filials,
            'vakancies':vakancies,
            'staffs':staffs
    })
    else:
        r = Register()
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        r.name = name
        r.phone = phone
        r.filial_id = int(address)
        r.save()
        return JsonResponse({'success':True,'errorMsg':'','_success': True})

# Create your views here.
