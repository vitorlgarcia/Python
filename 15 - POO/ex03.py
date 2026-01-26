class ContaBancaria:
    """
    Cria uma conta bancária com métodos para depositar, sacar e verificar o saldo.
    """
    def __init__(self, id, nome="", saldo=0.0): # Repare que self é obrigatório
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f"Conta bancária criada para {self.nome} com ID {self.id} e saldo inicial de R${self.saldo:,.2f}.")

    def depositar(self, valor): # REPARE que o primeiro parâmetro é sempre self
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} realizado com sucesso.") # usado o ,.2f para formatar o número com vírgula como separador de milhar e 2 casas decimais

    def sacar(self, valor): # Self representa a própria instância da classe
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso.")
        else:
            print(f"Saldo insuficiente na conta {self.id} para saque ou valor inválido.")

    def verificar_saldo(self):
        return f" O saldo da conta é: R${self.saldo:,.2f}"
    
    def __str__(self): # Representação da conta bancária
        return f"A conta Bancária de ID: {self.id}, do titular: {self.nome}, tem saldo de saldo: R${self.saldo:,.2f}."

c1 = ContaBancaria(id=1, nome="Vitor", saldo=1000.0)
c1.depositar(500.0)
c1.sacar(200.0)
print(c1) # Imprime a representação da conta bancária
print(c1.__doc__) # Imprime a docstring da classe ContaBancaria