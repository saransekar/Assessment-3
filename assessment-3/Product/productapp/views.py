from django.shortcuts import render, get_object_or_404
from django.template import loader  
from django.http import HttpResponse, HttpResponseNotFound 
from productapp.forms import ClientForm, ProductForm,RouterForm,HubForm
from productapp.models import Client,ProductImplementation,Router,Hub
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.exceptions import ValidationError
from django.urls import reverse


# Create your views here. 
@csrf_exempt
def createForm(request):

    if request.method == 'POST':
        client = ClientForm(request.POST)
        product = ProductForm(request.POST)        
        router = RouterForm(request.POST)
        hub = HubForm(request.POST)
        forms =[product,router,hub] 
       
        if client.is_valid():
            client_form = client.save(commit=False)
            client_form.save()
            for form in forms:
                form = form.save(commit=False)
                form.client = client_form
                form.save()               
            return render(request,'response.html',{'form':"Register is successfully"})  
        else:
            client = ClientForm(request.POST)
            product = ProductForm(request.POST)
            router = RouterForm(request.POST)
            hub = HubForm(request.POST)

            return render(request,'form.html', {'client': client, 'product':product, 'router':router, 'hub':hub})

    else:
        client = ClientForm()
        product = ProductForm()
        router = RouterForm()
        hub = HubForm()
        return render(request,'form.html', {'client': client, 'product':product, 'router':router, 'hub':hub})	



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
        template = loader.get_template('product.html')
        return HttpResponse(template.render({'client':client,'product_implement':product_implement,'router': router,'hub': hub})) 

    