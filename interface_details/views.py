from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import router
from .forms import routerform
from django.http import HttpResponse, JsonResponse
import rstr
import random

# Create your views here.


def create_view(request):

    context = {}
    form = routerform(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)

#redirect here
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = router.objects.get(sapid=id)

    return render(request, "detail_view.html", context)


# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(router, sapid=id)

    # pass the object as instance in form
    form = routerform(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):

    context = {}

    obj = get_object_or_404(router, sapid=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)


def gendata(request,id):
    id = int(id)
    data_out=[]

    if id > 1:
        for i in range(id):
            randString = generatedata()
            rtr=router()
            rtr.sapid = randString['sapid']
            rtr.hostname = randString['hostname']
            rtr.loopback = randString['loopback']
            rtr.mac_address = randString['mac_address']
            rtr.save()

            data = {
                'id': rtr.id,
                'sapid': randString['sapid'],
                'hostname': randString['hostname'],
                'loopback': randString['loopback'],
                'mac_address': randString['mac_address']
            }
            data_out.append(data)

        #detail = rtr.objects.get(id=rtr.id)




    else:
        randString = generatedata()
        rtr = router()
        rtr.sapid = randString['sapid']
        rtr.hostname = randString['hostname']
        rtr.ip_address = randString['loopback']
        rtr.mac_address = randString['mac_address']
        rtr.save()

        data = {
            'id': rtr.id,
            'sapid': randString['sapid'],
            'hostname': randString['hostname'],
            'loopback': randString['loopback'],
            'mac_address': randString['mac_address']
        }

        data_out.append(data)

    return JsonResponse(data_out, safe=False)

def generatedata():
    hostname = rstr.xeger("[\w\d]{10}")
    sapid = random.randint(1,999999999999999999)

    def ipAdd(n):
        ip_add = ''
        for i in range(n):
            num1 = random.random()
            num1 *= 1000
            ip_add += str(int(num1)) + '.'

        return ip_add[:-1]

    data = {
        'sapid': sapid,
        'hostname': hostname,
        'loopback': ipAdd(4),
        'mac_address': ipAdd(5)
    }

    return data





