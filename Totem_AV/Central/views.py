from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Principal(request):
    
        # Retrieve data for other form fields similarly

        # You can process the data here if needed
    if request.method == 'POST':
        # Retrieve form data from POST request
        sede = request.POST.get('Sede')
        boton1_nombre = request.POST.get('nombreBoton1')
        boton1_url = request.POST.get('urlBoton1')
        boton2_nombre = request.POST.get('nombreBoton2')
        boton2_url = request.POST.get('urlBoton2')
        boton3_nombre = request.POST.get('nombreBoton3')
        boton3_url = request.POST.get('urlBoton3')
        boton4_nombre = request.POST.get('nombreBoton4')
        boton4_url = request.POST.get('urlBoton4')
        # Render the result page
       
        return render(request, 'Central/HTML/Principal.html',{
            'sede': sede,
            'boton1_nombre': boton1_nombre,
            'boton1_url': boton1_url,
            'boton2_nombre': boton2_nombre,
            'boton2_url': boton2_url,
            'boton3_nombre': boton3_nombre,
            'boton3_url': boton3_url,
            'boton4_nombre': boton4_nombre,
            'boton4_url': boton4_url,
            # Add other data to the context
        })
    
    

def Totem(request):
    
    return render(request,'Central/HTML/Totem.html')