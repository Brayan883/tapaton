from collections import defaultdict
from email.policy import default
from django.shortcuts import render, redirect
from contabilidad.models import Tapa
from personal.forms import AprendizForm, AprendizUpdateForm, EquipoForm
from personal.models import Aprendiz, Equipo
from django.db.models import Sum
from django.contrib import messages

def aprendiz(request,pk=0):
    titulo_pagina="Aprendices"
    aprendices= Aprendiz.objects.all()

    if request.method == 'POST':
        form= AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            aprendiz_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El aprendiz {aprendiz_nombre} se agregó correctamente!')
            return redirect('personal-aprendiz')
    else:
        form= AprendizForm()
    context={
        "titulo_pagina": titulo_pagina,
        "aprendices": aprendices,
        "form":form
    }
    
    return render(request, "personal/aprendiz.html",context)
  

def aprendiz_update(request, pk):
    titulo_pagina="Aprendices"
    aprendices= Aprendiz.objects.all()

    aprendices_unique= Aprendiz.objects.get(id=pk)
    #items= Aprendiz.objects.raw('SELECT * FROM personal_aprendiz')
    if request.method == 'POST':
        form= AprendizUpdateForm(request.POST, instance=aprendices_unique)
        if form.is_valid():
            form.save()
            aprendiz_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El aprendiz {aprendiz_nombre} se agregó correctamente!')
            return redirect('personal-aprendiz')
    else:
        form= AprendizUpdateForm(instance=aprendices_unique)
    context={
        "titulo_pagina": titulo_pagina,
        "aprendices": aprendices,
        "form":form
    }
    return render(request, "personal/aprendiz-update.html",context)

def equipo(request):
    titulo_pagina="Equipos"
    equipos= Equipo.objects.all()
    
    puntos= list(Tapa.objects.values('aprendiz').annotate(puntos=Sum('cantidad')))
    for i in range(len(puntos) ):
        puntos[i]["aprendiz"]=Aprendiz.objects.get(id=puntos[i]["aprendiz"]).equipo
        puntos[i]["puntos"]=puntos[i]["puntos"]//15
    groups= defaultdict(list)
    
    for j in puntos:
        groups[j['aprendiz']].append(j)

    new_list= groups.values()
    finale=list()
    for k in new_list:
        aux={'equipo':0,'puntaje':0}
        for l in k:
           aux={'equipo':l['aprendiz'],'puntaje':l['puntos']+aux['puntaje']}
           
        finale.append(aux)
    print(finale)   
    
    if request.method == 'POST':
        form= EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            equipo_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El equipo {equipo_nombre} se agregó correctamente!')
            return redirect('personal-equipo')
        else:
            equipo_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'El equipo {equipo_nombre} no se ha podido agregar!')
           
            return redirect('personal-equipo')
    else:
        form= EquipoForm()
        context={
            "titulo_pagina":titulo_pagina,
            "equipos": equipos,
            "form": form,
            "puntos":finale
        }
    return render(request, "personal/equipo.html",context)

