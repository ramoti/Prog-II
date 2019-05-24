class Produto (object):

    def __init__ (self, nome, preco):

        self.nome =  nome
        self.preco = preco

class Item (Produto):

    def __init__ (self, produto, quantidade, peso):

        super().__init__ (preco) 
        self.produto = Produto 
        self.quantidade = quantidade
        self.peso = peso


class Carrinho (Item):

    def __init__ (self, data, hora, lista_itens):

        super().__init__ ()
        self. data = data
        self.hora = hora 
        self.lista_itens = lista_itens

    def mostrarCompras(self):

        for item in self.lista_itens :
            print (item)

if __name__ == "__main__" :

