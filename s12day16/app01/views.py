from django.shortcuts import render,HttpResponse



#Create your views here

def index(request,user):


    if request.method == 'GET':

        print("user request:" ,request.GET.get('user'))
        # return HttpResponse("welcome to payment index...%s" % user)
        return render(request,'app01/index.html')
    else:#post
        return HttpResponse("transfered 10000 to %s" %user)

def pay_by_cash(request):
    return HttpResponse("hello tuhao....")

def special_case_2003(request):
    print("matched 2003")

    return HttpResponse("matched...")

def year_archive(request,year,type,user):
    print("--->",type)
    return HttpResponse("%s %s %s" % (year, type, user))
def articles_detail(request,year,month,date,article_id,file_type):
    print("--->",year,month,file_type)
    return HttpResponse("%s/%s/%s--:[%s.%s]" % (year,month,date,article_id,file_type))