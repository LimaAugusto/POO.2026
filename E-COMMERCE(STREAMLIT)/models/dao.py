import json

class DAO:
    def __init__(self, classe, arquivo):
#       ATRIBUTOS DA CLASSE DAO:
        self._objetos = []        # <-- A LISTA DE OBJETOS COMO ATRIBUTO PROTEGIDO PARA QUE APENAS A CLASSE ESPECÍFICA POSSA CHAMAR AQUELA LISTA
        self.__classe = classe    # <-- CLASSE QUE HERDARÁ O DAO
        self.__arquivo = arquivo  # <-- ARQUIVO A SER USADO PARA LER E ESCREVER

    def inserir(self, obj):
        self.abrir() # CHAMA O MÉTODO ABRIR PARA ACESSAR O ARQUIVO DA LISTA
        if len(self._objetos) == 0: id = 0 # SE O TAMANHO DA LISTA = 0, ID = 0 
        else: id = (max(self._objeto, key = lambda x : x.getId())).getId + 1 # SE NÃO, PEGA O OBJETO COM MAIOR ID E SOMA MAIS 1
        obj.setId(id) # COM O (ID + 1), SETA ESSE COMO O ID DO OBJETO
        self._objetos.append(obj) # ADICIONA O OBJETO NA LISTA
        self.salvar() # CHAMA O MÉTODO SALVAR PARA SALVAR A NOVA LISTA COM O NOVO OBJETO NO ARQUIVO
    
    def salvar(self):
        with open(self._objetos, mode = "w") as arq: # COM O ARQUIVO ABERTO EM MODO DE ESCRITA:
            json.dumps(self._objetos, arq, default = self.__classe.to_json, ident = 4) # ESCREVE NO ARQUIVO E USA O "to_json" PARA SALVAR O DIC COMO STRING

    def abrir(self):
        self._objetos = [] # ESVAZIA A LISTA ANTES DE ABRIR
        try: # TENTA:
            with open(self.__arquivo, mode = "r") as arq: # COM O ARQUIVO ABERTO EM MODO DE LEITURA:
                list_dic = json.load(arq) # CARREGAR OS DADOS DO ARQUIVO PARA A VARIÁVEL "list_dic"
                for dic in list_dic: # DEPOIS USA UM LAÇO PARA PERCORRER CADA DICIONÁRIO/OBJETO, EM FORMATO STRING, NA LISTA 
                    obj = self.__classe.from_json(dic) # USA O MÉTODO "from_json" PARA TRANSFORMAR CADA OBJETO EM UM DADO ESTRUTURADO, UM DICIONÁRIO
                    self._objetos(obj) # E POR FIM, ADICIONA O OBJETO NA LISTA PROTEGIDA
        except FileNotFoundError: # EXCEÇÃO PARA TRATAR ERRO CASO O ARQUIVO NÃO EXISTA OU NÃO POSSA SER ACESSADO
            self._objetos = [] # SE O ERRO ACONTECER, ESVAZIA A LISTA

    def listar(self):
        self.abrir()
        return self._objetos # ABRE A LISTA E RETORNA A MESMA
    
    def listar_id(self, id):
        self.abrir() # RECEBE UM ID E ABRE O ARQUIVO
        for obj in self._objetos: # PERCORRE A LISTA DE OBJETOS
            if obj.getId() == id: return obj # VERIFICA SE O ID DO OBJETO É IGUAL O ID PASSADO
        return None # RETORNA "None" SE NÃO HOUVER ID CORRESPONDENTE

    def atualizar(self, obj):
        x = self.listar_id(obj.getId()) # RECEBE UM OBJ E CHAMA O LISTAR_ID PRA VERIFICAR SE EXISTE TAL OBJETO COM ESTE ID, ARMAZENA NA VARIÁVEL X
        if x != None: # SE HÁ, ENTÃO:
            self._objetos.remove(x) # REMOVE O OBJETO VELHO DA LISTA, NO CASO O QUE ESTÁ NA VARIÁVEL X
            self._objetos.append(obj) # DEPOIS ADICIONA O NOVO OBJETO
            self.salvar() # POR ÚLTIMO SLAVA O OBJETO NO ARQUIVO

    def excluir(self, obj):
        x = self.listar_id(obj.getId()) # RECEBE UM OBJETO E CHAMA O LISTAR_ID PARA VERIFICAÇÃO, COLOCA NA VARÁVEL X 
        if x != None: # SE HÁ, ENTÃO: 
            self._objetos.remove(x) # REMOVE O OBJETO DA LISTA
            self.salvar() # SALVA