from multiprocessing.sharedctypes import Value

from django.forms import model_to_dict
from .models import Transation


def handle_uploaded_file(f):
    for lines in f.readlines():
        tipo = lines[0:1].decode("utf-8")
        data = lines[1:9].decode("utf-8")
        value = lines[10:19].decode("utf-8")
        cpf = lines[20:30].decode("utf-8")
        card = lines[31:42].decode("utf-8")
        hour = lines[43:48].decode("utf-8")
        shop_owner = lines[48:62].decode("utf-8").replace("\n","")
        shop_name = lines[62:81].decode("utf-8").replace("\n","")
        transation_obj = {"tipo": tipo,"data": data,"valor": value,"cpf": cpf,
        "cartao": card,"hora": hour,"dono_da_loja": shop_owner,"nome_da_loja": shop_name.strip()}
        Transation.objects.create(**transation_obj)

def handle_value(list):
    value = 0
    for l in list:
        if l['tipo'] == 2 or l['tipo'] == 3 or l['tipo'] == 9:
            value -= int(l['valor'])
        else:
            value += int(l['valor'])
    return value
