from models.dao import DAO

STATUS_VALIDOS = ["Pendente", "Em Trânsito", "Entregue"]

class Entrega:
    def __init__(self, id, id_venda, id_entregador, status = "Pendente"):
        self.setId(id)
        self.setId_Venda(id_venda)
        self.setId_Entregador(id_entregador)
        self.setStatus(status)

    #----- GETTERS -----

    def getId(self):
        return self.id

    def getId_Venda(self):
        return self.id_venda

    def getId_Entregador(self):
        return self.id_entregador

    def getStatus(self):
        return self.status

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setId_Venda(self, id_venda):
        if id_venda < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_venda = id_venda

    def setId_Entregador(self, id_entregador):
        if id_entregador < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_entregador = id_entregador

    def setStatus(self, status):
        if status not in STATUS_VALIDOS:
            raise ValueError(f"STATUS INVÁLIDO! USE: {', '.join(STATUS_VALIDOS)}")
        self.status = status

    #----- SETTERS -----

    #----- HELPERS -----

    def proximo_status(self):
        # RETORNA O PRÓXIMO STATUS NA SEQUÊNCIA, OU None SE JÁ ESTIVER NO FINAL
        idx = STATUS_VALIDOS.index(self.status)
        if idx < len(STATUS_VALIDOS) - 1:
            return STATUS_VALIDOS[idx + 1]
        return None

    #----- HELPERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"ENTREGA_ID: {self.id} | VENDA: {self.id_venda} | ENTREGADOR: {self.id_entregador} | STATUS: {self.status}"

    #----- TO_STRING -----

    # ----- TO_JSON -----

    def to_json(self):
        return { "id": self.id, "id_venda": self.id_venda, "id_entregador": self.id_entregador, "status": self.status }

    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Entrega(dic["id"], dic["id_venda"], dic["id_entregador"], dic["status"])

    # ----- FROM_JSON -----


class EntregaDAO(DAO):
    def __init__(self):
        super().__init__(Entrega, "entregas.json")

    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x: x.getId())
        return objetos

    def listar_por_entregador(self, id_entregador):
        return [e for e in self.listar() if e.getId_Entregador() == id_entregador]

    def listar_por_venda(self, id_venda):
        return [e for e in self.listar() if e.getId_Venda() == id_venda]
