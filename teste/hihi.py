class Receita(BaseModel):
    nome = CharField()
class Ingrediente(BaseModel):
    nome = CharField()
    unidade = CharField()
class IngredienteDaReceita(BaseModel):
    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    quantidade = FloatField()
    
bolo = Receita.create(nome = "Bolo de laranja")
ovo = Ingrediente.create(nome = "Ovo", unidade = "unidade")
xicoleo = Ingrediente.create(nome = "Óleo", unidade = "xícara")
ing1 = IngredienteDaReceita(receita = bolo,
ingrediente = ovo, quantidade = 4.0)
ing2 = IngredienteDaReceita(receita = bolo,
ingrediente = xicoleo, quantidade = 1.0)
print(ing1.receita.nome, ing1.ingrediente.nome,
88
ing1.ingrediente.unidade, ing1.quantidade)