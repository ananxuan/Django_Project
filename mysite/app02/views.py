from django.shortcuts import render,HttpResponse,render_to_reponse
from app02 import models




def home(request):
    return HttpResponse("app02.home")

def db_handle(request):
    #增加
    # models.UserInfo.objects.create(username= 'xuan', password= '123',age= 18)
    # request.POST #以post方式提交
    # request.GET
    # dic = {'username': 'xuan1', 'password': '123','age':18}
    # models.UserInfo.objects.create(**dic)
    #
    # #delete
    # models.UserInfo.objects.filter(username= 'xuan').delete()
    # #modify
    # models.UserInfo.objects.all().update(age = 20)
    # #search
    # models.UserInfo.objects.filter(age= 18)

    # for line in user_list_obj:
    #     print(line.username)

    # return HttpResponse('ok')
    if request.method == "POST":
        print(request.POST)
        # request.POST['age'] = int(request.POST['age'])
        # d = dict(request.POST)
        # models.UserInfo.objects.create(**d)
        models.UserInfo.objects.create(username = request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])
    user_list_obj = models.UserInfo.objects.all()
    return render(request,'t1.html',{'li':user_list_obj})
    
#show all reuqest.META data
def dispaly_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

#create a search chart
def search_form(request):
    return render_to_response('search_form.html')
