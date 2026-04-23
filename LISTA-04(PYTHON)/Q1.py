class Musica :
    def __init__(self, titulo, artista, album) :
        self.SetTitulo(titulo)
        self.SetArtista(artista)
        self.SetAlbum(album)
    def SetTitulo(self, v) :
        self.__titulo = v
        return self.__titulo
    def SetArtista(self, v) :
        self.__artista = v
        return self.__artista
    def SetAlbum(self, v) :
        self.__album = v
        return self.__album
    
    def GetTitulo(self) :
        return self.__titulo
    def GetArtista(self) :
        return self.__artista
    def GetAlbum(self) :
        return self.__album
    
    def __str__(self) :
        return f"Título: {self.__titulo} -- Artista: {self.__artista} -- Álbum: {self.__album}"

class PlayList :
    def __init__(self, nome, descricao) :
        self.SetNome(nome)
        self.SetDescricao(descricao)
        self.__musicas = []
    def SetNome(self, v) :
        self.__nome = v
        return self.__nome
    def SetDescricao(self, v) :
        self.__descricao = v
        return self.__descricao
    def Inserir(self, Musica) :
        self.__musicas.append(Musica)
        return self.__musicas
    def Listar(self) :
        if len(self.__musicas) > 0 :
            for musica in self.__musicas :
                print (musica)
        else : return ValueError("Lista Vazia")
    
    def __str__(self) :
        return f"Minha PlayList: {self.__nome}, {self.__descricao}"

class UI :
    @staticmethod
    def main() :
        playlist1 = PlayList("Hits", "Hits do momento")
        m1 = Musica("Shape of You", "Ed Sheeran", "Deluxe")
        m2 = Musica("Show Me How To Live", "AudioSlave", "Show How To Live")
        m3 = Musica("teste", "teste", "teste")
        playlist1.Inserir(m1)
        playlist1.Inserir(m2)
        playlist1.Inserir(m3)
        print(playlist1)
        playlist1.Listar()

UI.main()