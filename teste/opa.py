class Pessoa ():
    
    def __init__ (self, nome, rua, numero):
        self.nome = nome
        self.rua = rua
        self.numero = numero

if __name__ == "__main__":
    mariana = Pessoa ("Mariana" , "araçai" , "1234-1234")
    print (mariana.nome, ",", mariana.rua, ",", mariana.numero)