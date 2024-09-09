from django.shortcuts import render

def main(request):
    data={"nombre":"Camilo","apellido":"Mimiza"}
    return render(request,'myapp/index.html',data)
# Create your views here.
