from django.shortcuts import render
from django.template import loader  
from django.http import HttpResponse, HttpResponseNotFound 
from productapp.forms import ClientForm,ProductForm,RouterForm,HubForm
from productapp.models import Client,ProductImplementation,Router,Hub
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ValidationError
# Create your views here.

# def createForm(request):
#     client = ClientForm()
#     product = ProductForm()
#     router = RouterForm()
#     hub = HubForm()
#     return render(request,'form.html',{'client':client, 'product':product,'router':router,'hub':hub})    
    
@csrf_exempt
def createForm(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        client = ClientForm(request.POST)
        product = ProductForm(request.POST)
        router = RouterForm(request.POST)
        hub = HubForm(request.POST)
        if client.is_valid():
            client_name = request.POST["client_name"]
            contact_name = request.POST["contact_name"]
            client_code = request.POST["client_code"]
            mobile_number = request.POST["mobile_number"]
            installation_date = request.POST["installation_date"]
            wireless_router_ip = request.POST["wireless_router_ip"]
            hub_ip = request.POST["hub_ip"]

            context = {
                'client_name'   : client_name,
                'contact_name'  : contact_name,
                'client_code'   : client_code,
                'mobile_number' : mobile_number,
                'installation_date' : installation_date,
                'wireless_router_ip' : wireless_router_ip,
                'hub_ip'    : hub_ip

            }
            client = Client.objects.create(client_name=client_name,contact_name=contact_name,client_code=client_code,mobile_number=mobile_number)  
            client.save()
            client_id = Client.objects.get(client_code=client_code) 
            client_id = client_id.id
            product = ProductImplementation.objects.create(client_id=client_id,installation_date = installation_date)
            product.save()
            router = Router.objects.create(client_id=client_id,wireless_router_ip=wireless_router_ip)
            router.save()
            hub = Hub.objects.create(client_id=client_id,hub_ip=hub_ip)
            hub.save()
            return render(request,'response.html',{'form':"Register is successfully"})  

        else:
            client = ClientForm(request.POST)
            product = ProductForm(request.POST)
            router = RouterForm(request.POST)
            hub = HubForm(request.POST)
            return render(request,'form.html', {'client': client,'product':product,'router':router,'hub':hub})

    else:
        client = ClientForm()
        product = ProductForm()
        router = RouterForm()
        hub = HubForm()
        return render(request,'form.html', {'client': client,'product':product,'router':router,'hub':hub})	



def viewData(request):
    clients = []
    client = Client.objects.all()
    client_list = list(client)
    template = loader.get_template('view.html')
    return HttpResponse(template.render({'client_list':client_list})) 

def index(request):
    return render(request,'index.html')  

@csrf_exempt
def fetchData(request):
    if request.method == 'POST':
        client_id = request.POST["client"]
        client = Client.objects.get(id=client_id)
        product_implement = client.productimplementation_set.all()
        router = client.router_set.all()
        hub = client.hub_set.all()
        # client_data = Client.objects.all()
        template = loader.get_template('product.html')
        return HttpResponse(template.render({'client':client,'product_implement':product_implement,'router': router,'hub': hub})) 

        # return HttpResponse(clients)