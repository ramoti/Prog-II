class Pessoa ():
    
    def __init__ (self, nome, endereco, telefone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf

if __name__ == "__main__":
    mariana = Pessoa ("Mariana" , "araçai" , "1234-1234" , "456.456.456-35")
    print (mariana.nome, ",", mariana.rua, ",", mariana.numero, "," , mariana.cpf)