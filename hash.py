class TabelaHash:
    def __init__(self, tamanho=10):

        self.tamanho = tamanho
        self.tabela = [None] * tamanho

        def funcao_hash(self, chave):
            soma = 0
            for letra in chave:
                soma += ord(letra)
                return soma % self.tamanho
            
        def inserir(self, chave, valor):
            indice = self.funcao_hash(chave)

# AINDA NÃO FOI TERMINADO O CÓDIGO

# tabela = TabelaHash()

#tabela.inserir("nome", "Welterson")
#tabela.inserir("idade", 22)
#tabela.inserir("cidade", "Guanambi")

#print(tabela.buscar("nome"))  # Saída: Welterson
#print(tabela)