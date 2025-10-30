from hashlib import sha256

class TabelaHash:
    class Elemento:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor

    def __init__(self):
        self.capacidade_atual = 5
        self.tabela_initerna = [[] for _ in range(self.capacidade_atual)]
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    

    def verificar_chave(self, chave):
        hash(chave)
    

    def hash_deterministico(chave):
        codificado = str(chave).encode()
        return int(sha256(codificado).hexdigest(), 16)
    

    def descobrir_indice(self, chave):
        return self.hash_deterministico(chave) % self.capacidade_atual
    
    def __setitem__(self, chave, valor):
        self.verificar_chave(chave)

        indice = self.descobrir_indice(chave)

        # Verificando se a chave já existe na tabela
        for elemento in self.tabela_initerna[indice]:
            if elemento.chave == chave:
                elemento.valor = valor  # se ele encontrar, vai atualizar o valor
                return 
            
        # Se não encontrar, deve adicionar um novo valor
        novo_elemento = self.Elemento(chave, valor)
        self.tabela_initerna[indice].append(novo_elemento)
        self.tamanho += 1
    


aluno = TabelaHash()

aluno['nome'] = 'Welterson'
aluno['RA'] = 1012420627
aluno['curso'] = 'ciencia da computacao'
aluno['professor'] = 'hissamu'
aluno['uc'] = 'estrutura de dados'
aluno['semestre'] = 3

print(f'Quantidade de elementos: {len(aluno)}')