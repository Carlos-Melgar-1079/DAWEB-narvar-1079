from django.shortcuts import render,redirect
from .models import venta

# Create your views here.

def inicio_vistaventas(request):
    losventas = venta.objects.all()

    return render(request,"gestionarventa.html",{"misventas":losventas})



def registrarventa(request):
    id_venta = request.POST["txtidventa"]
    fecha = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    id_cliente= request.POST["txtidcliente"]
    id_producto = request.POST["txtidproducto"]
    id_empleado = request.POST["txtidempleado"]
    total = request.POST["txttotal"]

    guardarventa = venta.objects.create(id_venta=id_venta, fecha=fecha, cantidad=cantidad, id_cliente=id_cliente,
                                            id_producto=id_producto,  id_empleado=id_empleado, total=total)

    return redirect("ventas")

def seleccionarventa(request, id_venta):
    ventar = venta.objects.get(id_venta = id_venta)

    return render(request,"editarventa.html",{"misventas":ventar})


def editarventa(request):
    id_venta = request.POST["txtidventa"]
    fecha = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    id_cliente= request.POST["txtidcliente"]
    id_producto = request.POST["txtidproducto"]
    id_empleado = request.POST["txtidempleado"]
    total = request.POST["txttotal"]
    

    ventas = venta.objects.get(id_venta = id_venta)
    ventas.fecha = fecha
    ventas.cantidad = cantidad
    ventas.id_producto = id_cliente
    ventas.id_producto = id_producto
    ventas.id_empleado = id_empleado
    ventas.total=total
    

    ventas.save()

    return redirect("ventas")


def borrarventa(request, id_venta):
    ven = venta.objects.get(id_venta = id_venta)
    ven.delete()

    return redirect("ventas")