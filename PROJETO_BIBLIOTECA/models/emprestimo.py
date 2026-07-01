from datetime import date
from entidade import Entidade


class Emprestimo(Entidade):

    def __init__(self, id, dataEmprestimo, dataDevolucao, valorMulta=0):
        super().__init__(id)
        self.setDataEmprestimo(dataEmprestimo)
        self.setDataDevolucao(dataDevolucao)
        self.setValorMulta(valorMulta)

    def getDataEmprestimo(self):
        return self.dataEmprestimo

    def getDataDevolucao(self):
        return self.dataDevolucao

    def getValorMulta(self):
        return self.valorMulta

    def setDataEmprestimo(self, dataEmprestimo):
        if isinstance(dataEmprestimo, date):
            self.dataEmprestimo = dataEmprestimo
        else:
            raise TypeError("A data do empréstimo deve ser do tipo date.")

    def setDataDevolucao(self, dataDevolucao):
        if isinstance(dataDevolucao, date):
            self.dataDevolucao = dataDevolucao
        else:
            raise TypeError("A data da devolução deve ser do tipo date.")

    def setValorMulta(self, valorMulta):
        if isinstance(valorMulta, (int, float)):
            self._valorMulta = valorMulta
        else:
            raise TypeError("O valor da multa deve ser um número.")

    def __str__(self):
        return (
            f"Empréstimo\n"
            f"ID: {self.getId()}\n"
            f"Data do Empréstimo: {self.getDataEmprestimo()}\n"
            f"Data da Devolução: {self.getDataDevolucao()}\n"
            f"Valor da Multa: R$ {self.getValorMulta():.2f}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "dataEmprestimo": self.getDataEmprestimo(),
            "dataDevolucao": self.getDataDevolucao(),
            "valorMulta": self.getValorMulta()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["dataEmprestimo"],
            dados["dataDevolucao"],
            dados["valorMulta"]
        )