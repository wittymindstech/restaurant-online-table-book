from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import BookTable,Order
def index(request):
    return render(request, "index.html")
@csrf_exempt
def bill(req):
    print("inside bill")
    if req.method=='POST':
        print('inside post')
        amount=str(req.POST.get('price'))
        amount=amount.split('$')
        amount=float(amount[1])
        print(amount)

        name=str(req.POST.get('name'))
        print(name,amount)
        table_id=req.POST.get('table_num')
        print("table num",table_id)
        peoples=req.POST.getlist('values[]')
        print(peoples)
        print(len(peoples))
        num_of_persons=len(peoples)
        # print(len(peoples))
        each_contribution=amount/num_of_persons
        print(each_contribution)


        order_id=str(req.POST.get('order_id'))
        print("order_id",order_id)
        order_id=int(order_id)
        print(order_id)
        if Order.objects.filter(order_id=order_id):
            print('inside already exits')
            d=Order.objects.get(order_id=order_id)
            print(d.each_contribution)
            list_of_members=json.loads(d.each_contribution)
            print(list_of_members)
            for p in peoples:
                if p in list_of_members.keys():

                    list_of_members[p]+=each_contribution
                else:
                    list_of_members[p]=each_contribution
            print('order already exists')
            print(d.total_amount)
            total_amount=float(d.total_amount)
            total_amount+=float(amount)
            print(list_of_members)
            Order.objects.filter(order_id=order_id).update(total_amount=str(total_amount),each_contribution=json.dumps(list_of_members))

        else:
            d={}
            for p in peoples:
                d[str(p)]=each_contribution
            print(d)
            Order(order_id=int(order_id),table_id=1,booking_name='hy',total_amount=str(amount),each_contribution=json.dumps(d)).save()
        # print(peoples)
        # print(len(peoples))
        return JsonResponse({'status':True})
    return render(req,'bill.html')
def shopingcart(req):
    return render(req,'shopingcart.html')
def search(req):
    if req.method=='GET':
        name=req.GET['search']
        return render(req,'search.html',{'name':name})
    return render(req,'search.html')
def reservation(req):
    if req.method=='GET':
        name=req.GET.get('name')
        date=req.GET.get('date')
        time=req.GET.get('time')
        email=req.GET.get('email')
        num_of_persons=req.GET.get('num_of_persons')
        print(num_of_persons)
        cont_num=req.GET.get('phone')
        print('inside get')
        message='booking process is start please check your mail'
        BookTable(name=name, table_book_time=time,table_book_date=date,num_of_person=num_of_persons,contact_num=cont_num,email=email).save()
        print(name,email,date,time,num_of_persons,cont_num)
        return render(req,'reservation.html',{'message':message})
    print('inside reservation')
    return render(req,'reservation.html')
@csrf_exempt
def adminPage(req):

    if req.method=='POST':
        id=req.POST.get('id')
        print(id)
        id=BookTable.objects.filter(pk=id)
        print(id)
        obj=BookTable.objects.filter(status=False)
        print('inside admin table')
        return render(req,'admintable.html',{'obj':obj})
    obj=BookTable.objects.filter(status=False)
    return render(req,'admintable.html',{'obj':obj})
def final_bill(req):
    if req.method=='POST':
        id=req.POST.get('id')
        id=int(id)
        obj=Order.objects.get(order_id=id)
        l=[]
        value=[]
        for i in obj.each_contribution:
            l.append(i)



        return render(req,'finalbill.html',{'obj':obj,'name':l})
    return render(req,'finalbill.html')
def admin(req):
    return render(req,'admin_section/index.html')
def inside(req):
    return render(req,'inside.html')
def booking(request):
    return render(request, "detail-booking.html")

def about(req):
    return render(req,'about.html')
def menu(req):
    return render(req,'menu.html')
def success(request):
    return render(request, "confirm.html")
