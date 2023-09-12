class Funcionario:
    def __init__(self, matricula, nome, cargo):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo


class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, matricula):
        matricula_int = int(str(matricula).lstrip('0'))
        return matricula_int % self.tamanho

    def inserir(self, funcionario):
        posicao = self.hash(funcionario.matricula)
        self.tabela[posicao].append(funcionario)

    def deletar(self, matricula):
        posicao = self.hash(matricula)
        for funcionario in self.tabela[posicao]:
            if funcionario.matricula == matricula:
                self.tabela[posicao].remove(funcionario)

    def buscar(self, matricula):
        posicao = self.hash(matricula)
        for funcionario in self.tabela[posicao]:
            if funcionario.matricula == matricula:
                return funcionario

    def imprimir_funcionarios(self):
        for lista in self.tabela:
            for funcionario in lista:
                print(
                    f"Matrícula: {funcionario.matricula}, Nome: {funcionario.nome}, Cargo: {funcionario.cargo}")


tamanho = 1000
tabela_hash = TabelaHash(tamanho)

# funcionario1 = Funcionario("00000", "Funcionário 0", "Cargo 0")
funcionario1 = Funcionario("00001", "Funcionário 1", "Cargo 1")
funcionario2 = Funcionario("01000", "Funcionário 1000", "Cargo 1000")
funcionario3 = Funcionario("01001", "Funcionário 1001", "Cargo 1001")

tabela_hash.inserir(funcionario1)
tabela_hash.inserir(funcionario2)
tabela_hash.inserir(funcionario3)

funcionario = tabela_hash.buscar("00001")
if funcionario:
    print(
        f"Funcionário encontrado: {funcionario.nome} <{funcionario.matricula}>")
else:
    print("Funcionário não encontrado.")

print("\n")

tabela_hash.imprimir_funcionarios()

tabela_hash.deletar("00001")

print("\n")

tabela_hash.imprimir_funcionarios()
