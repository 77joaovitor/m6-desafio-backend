    
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

from form.models import Transation
from .forms import UploadFileForm, ValueFileForm
from django import template
register = template.Library()

from .utils import handle_uploaded_file, handle_value

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('sucesso!')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def sucess(request):
    if request.method == 'POST':
        form = ValueFileForm(request.POST)
        if form.is_valid():
            tran = Transation.objects.filter(nome_da_loja=request.POST.get('title'))
            list = []
            for tr in tran:
                dict = model_to_dict(tr)
                list.append(dict)
            value_total = handle_value(list)

            render(list, 'value.html')
            return HttpResponse(f' "Saldo da Loja": R${value_total}' )
    else:
        form = ValueFileForm()
    return render(request, 'value.html', {'form': form})
        

