from models.dao import DAO
from datetime import datetime

class Promocao:
    def __init__(self, id, id_categoria, data_inicio, data_fim, percentual):
        self.setId(id)
        self.setId_Categoria(id_categoria)
        self.setData_Inicio(data_inicio)
        self.setData_Fim(data_fim)
        self.setPercentual(percentual)

    #----- GETTERS -----

    def getId(self):
        return self.id

    def getId_Categoria(self):
        return self.id_categoria

    def getData_Inicio(self):
        return self.data_inicio

    def getData_Fim(self):
        return self.data_fim

    def getPercentual(self):
        return self.percentual

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setId_Categoria(self, id_categoria):
        if id_categoria < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_categoria = id_categoria

    def setData_Inicio(self, data_inicio):
        if isinstance(data_inicio, str):
            self.data_inicio = datetime.fromisoformat(data_inicio)
        else:
            self.data_inicio = data_inicio

    def setData_Fim(self, data_fim):
        if isinstance(data_fim, str):
            self.data_fim = datetime.fromisoformat(data_fim)
        else:
            self.data_fim = data_fim

    def setPercentual(self, percentual):
        if percentual <= 0 or percentual > 100:
            raise ValueError("PERCENTUAL INVÁLIDO! DEVE SER ENTRE 0 E 100.")
        self.percentual = percentual

    #----- SETTERS -----

    #----- HELPERS -----

    def esta_ativa(self):
        # VERIFICA SE A PROMOÇÃO ESTÁ ATIVA NO MOMENTO ATUAL
        agora = datetime.now()
        return self.data_inicio <= agora <= self.data_fim

    #----- HELPERS -----

    #----- TO_STRING -----

    def __str__(self):
        return (f"PROMOÇÃO_ID: {self.id} | CATEGORIA: {self.id_categoria} | "
                f"INÍCIO: {self.data_inicio.strftime('%d/%m/%Y')} | "
                f"FIM: {self.data_fim.strftime('%d/%m/%Y')} | "
                f"DESCONTO: {self.percentual}%")

    #----- TO_STRING -----

    # ----- TO_JSON -----

    def to_json(self):
        return {
            "id": self.id,
            "id_categoria": self.id_categoria,
            "data_inicio": self.data_inicio.isoformat(),
            "data_fim": self.data_fim.isoformat(),
            "percentual": self.percentual
        }

    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Promocao(dic["id"], dic["id_categoria"], dic["data_inicio"], dic["data_fim"], dic["percentual"])

    # ----- FROM_JSON -----


class PromocaoDAO(DAO):
    def __init__(self):
        super().__init__(Promocao, "promocoes.json")

    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x: x.getId())
        return objetos

    def listar_ativas_por_categoria(self, id_categoria):
        # RETORNA TODAS AS PROMOÇÕES ATIVAS PARA UMA CATEGORIA ESPECÍFICA
        return [p for p in self.listar() if p.getId_Categoria() == id_categoria and p.esta_ativa()]