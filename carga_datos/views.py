from django.shortcuts import render, redirect
from carga_datos.forms import UploadForm
from carga_datos.models import archivo

# Create your views here.
def cargacatalogo(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = archivo(nombre_archivo = request.POST['nombre_archivo'],ubicacion_archivo = request.FILES['ubicacion_archivo'])
            newdoc.save(form)
            return redirect("uploads")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'carga_archivo.html', {'form': form})