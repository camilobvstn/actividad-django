from django.shortcuts import render

def main(request):
    return render(request,'myapp/index.html')

def electronica(request):
    data={"tituloprod":"Electronica","prod1":"Mac","prod2":"iPhone","prod3":"Playstation"
          , "img_1":"img/bbb.png","img_2":"img/clairo.jpg"}
    return render(request,'myapp/productos.html',data)

def juguetes(request):
    data={"tituloprod":"Juguetes","prod1":"Auto","prod2":"Pelota de futbol","prod3":"Figura de accion",
          "img_1":"img/bbb2.jpg", "img_2":"img/marias.jpg"}
          
    return render(request,'myapp/productos.html',data)

def ropa(request):
    data={"tituloprod":"Ropa","prod1":"Jeans","prod2":"Pantalon","prod3":"Gorro",
          "img_1":"img/tv.jpg", "img_2":"img/marias.jpg"}
          
    return render(request,'myapp/productos.html',data)

# Create your views here.
