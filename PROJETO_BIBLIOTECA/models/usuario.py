from entidade import Entidade

class Usuario(Entidade):
    def __init__(self, id, nome, cpf, email, senha, telefone):
        super.__init__(id)
        self.setNome(nome)
        self.setCpf(cpf)
        self.setEmail(email)
        self.setSenha(senha)
        self.setTelefone(telefone)

    def getNome(self):
        return self.nome    
    def getCpf(self):
        return self.cpf    
    def getEmail(self):
        return self.email   
    def getSenha(self):
        return self.senha   
    def getTelefone(self):
        return self.telefone


    def setNome(self, v):
        if isinstance(v, str): self.nome = v
        else: raise ValueError("APENAS STRING.")
    def setCpf(self, v):
        if isinstance(v, str): self.cpf = v
        else: raise ValueError("APENAS STRING.")
    def setEmail(self, v):
        if isinstance(v, str): self.email = v
        else: raise ValueError("APENAS STRING.")
    def setSenha(self, v):
        if isinstance(v, str): self.senha = v
        else: raise ValueError("APENAS STRING.")
    def setTelefone(self, v):
        if isinstance(v, str): self.telefone = v
        else: raise ValueError("APENAS STRING.")

    def __str__(self):
        return (
            f"Usuário\n"
            f"ID: {self.getId()}\n"
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"E-mail: {self.email}\n"
            f"Telefone: {self.telefone}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "nome": self.getNome(),
            "cpf": self.getCpf(),
            "email": self.getEmail(),
            "senha": self.getSenha(),
            "telefone": self.getTelefone()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["nome"],
            dados["cpf"],
            dados["email"],
            dados["senha"],
            dados["telefone"]
        )