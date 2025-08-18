from django.http import HttpResponse

def mostrar_bienvenida(request):
 nombre = "Test"
 return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")