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
        # Render the result page
       
        return render(request, 'Central/HTML/Principal.html',{
            'sede': sede,
            'boton1_nombre': boton1_nombre,
            'boton1_url': boton1_url,
            # Add other data to the context
        })
    
    

def Totem(request):
    
    return render(request,'Central/HTML/Totem.html')