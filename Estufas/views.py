from django.shortcuts import render, get_object_or_404
from Estufas.models import Estufa

# Create your views here.
def estufas(request):

    estufas = Estufa.objects.all()

    return render(request, 'estufas/index.html', {'estufas':estufas})

def estufa_detalle(request, id):

    estufa = get_object_or_404(Estufa, id=id)

    return render(request, 'estufas/estufa_detalle.html', {'estufa': estufa})