from models.dao import DAO
import json
from datetime import datetime

# ESSE CONVERSOR VERIFICA SE O OBJETO É DO TIPO DATETIME:
# SE SIM, ELE RETORNA O OBJETO, AGORA TRANSFORMADO EM STRING NO FORMATO ISO(INTERNACIONAL).
# SE NÃO, ELE USA O VARS PARA RETORNAR OS ATRIBUTOS NORMAIS DO OBJETO, COMO UMA STRING, POR EXEMPLO.
def conversor_json(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return vars(obj) 

class Venda:
    def __init__(self, id, data, total, id_cliente):
#       ATRIBUTOS DA CLASSE VENDA:
        self.setId(id)                  # <-- ID DA VENDA
        self.setData(data)              # <-- DATA EM QUE OCORREU A VENDA
        self.setTotal(total)            # <-- PREÇO TOTAL DA VENDA
        self.setId_Cliente(id_cliente)  # <-- ID DO CLIENTE

    #----- GETTERS -----

    def getId(self):
        return self.id
    
    def getData(self):
        return self.data
    
    def getTotal(self):
        return self.total
    
    def getId_Cliente(self):
        return self.id_cliente

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setData(self, data):
        if isinstance(data, str): # Se a data for uma string:
            try:
                self.data = datetime.fromisoformat(data) # Tenta passar para o formato ISO(internacional) EX.: 2026-05-26 15:30:00
            except ValueError: # Se for uma string e não estiver no padrão internacional, ele tenta forçar para o formato brasileiro: DD/MM/AAAA HH:MM
                self.data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        else: self.data = data # Se não for uma string, pode ser um núemro, etc. ele apenas atribui o valor ao self.data

    def setTotal(self, total):
        if total < 0: raise ValueError("VALOR INVÁLIDO!")
        self.total = total

    def setId_Cliente(self, id_cliente):
        if id_cliente < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_cliente = id_cliente

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"VENDA_ID: {self.id}  DATA: {self.data}  TOTAL: R${self.total:.2f}  ID_CLIENTE: {self.id_cliente}"

    #----- TO_STRING -----

    # ----- TO_JSON -----

    def to_json(self):
        return { "id" : self.id, "data" : self.data.isoformat(), "total" : self.total, "id_cliente" : self.id_cliente }
    
    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Venda(dic["id"], dic["data"], dic["total"], dic["id_cliente"])
    
    # ----- FROM_JSON -----

class VendaDAO(DAO):
#   CHAMA OS ATRIBUTOS DA VENDA E DEFINE O ARQUIVO A SER USADO PARA LER E ESCREVER
    def __init__(self):
        super().__init__(Venda, "vendas.json")

#   CHAMA O MÉTODO LISTAR DA CLASSE SUPER NO DAO E ORGANIZA POR ID DE VENDA
    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.getId())
        return objetos