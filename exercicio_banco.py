tipo_deposito = 'Depósito'
tipo_saque = 'Saque'
tipo_feminino = 'F'
tipo_masculino = 'M'

class Banco:
    def __init__(self, agencia):
        self.__agencia = agencia
        self.__contas = []
    @property
    def agencia(self):
        return self.__agencia
    @property
    def contas(self):
        return self.__contas
    
    def add_conta(self, conta):
        self.__contas.append(conta)

class Cliente:
    def __init__(self, nome, telefone, renda_mensal, sexo):
        self.__nome = nome 
        self.__telefone = telefone
        self.__renda_mensal = renda_mensal
        self.__sexo = sexo

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def sexo(self):
        return self.__sexo

class Operacao:
    def __init__(self, tipo_operacao, valor):
        self.__tipo_operacao = tipo_operacao
        self.__valor = valor
    
    @property
    def tipo_operacao(self):
        return self.__tipo_operacao

    @property
    def valor(self):
        return self.__valor
class Deposito(Operacao):
    def __init__(self, valor):
        super().__init__(tipo_deposito, valor)

class Saque(Operacao):
    def __init__(self, valor):
        super().__init__(tipo_saque, valor)

class Conta:
    def __init__(self, titulares, numero_conta, agencia):
        self.__titulares = titulares
        self.__numero_conta = numero_conta
        self.__agencia = agencia
        self.__operacoes = []
        self.__saldo_conta = 0

    @property
    def conta(self):
        return self.__numero_conta
    @property
    def agencia(self):
        return self.__agencia
    @property
    def titulares(self):
        return self.__titulares
    
    @property
    def saldo_conta(self):
        return self.__saldo_conta

    @property
    def operacoes(self):
        return self.__operacoes
    
    @property
    def limite_cheque_especial(self):
        total_limite = 0
        total_titulares_mulheres = 0
        for cliente in self.titulares:
            if cliente.sexo == tipo_feminino:
                total_limite += cliente.renda_mensal
                total_titulares_mulheres +=1 
        return total_limite / total_titulares_mulheres

    @property
    def limite_saque(self):
        return self.limite_cheque_especial + self.saldo_conta

    def depositar(self, valor):
        self.__operacoes.append(Deposito(valor))
        self.atualizar_saldo()

    def sacar (self, valor):
        if self.limite_saque > valor:
            self.__operacoes.append(Saque(valor))  
            self.atualizar_saldo()

    def atualizar_saldo(self):
        total_saldo = 0
        for operacao in self.operacoes:
            if operacao.tipo_operacao == tipo_deposito:
                total_saldo += operacao.valor
            if operacao.tipo_operacao == tipo_saque:
                total_saldo -= operacao.valor
        self.__saldo_conta = total_saldo
    
    def extrato(self):
        print('Seu extrato é: ')
        print('---------------')
        for operacao in self.operacoes:
            if operacao.tipo_operacao == tipo_deposito:
                print(f'{operacao.tipo_operacao}....{operacao.valor}')
            if operacao.tipo_operacao == tipo_saque:
                print(f'{operacao.tipo_operacao}.......{operacao.valor}')
        print('---------------')
        print(f'Seu saldo é: {self.saldo_conta}')
        print(f'Seu limite é: {self.limite_cheque_especial}')
        print(f'Seu limite para saque é: {self.limite_saque}')



banco_delas = Banco('001')
titular_1 = Cliente('Naiara', '(42) 991223366', 5000, 'F')
titular_2 = Cliente('João', '(42) 1234560', 10000, 'M')
minha_conta = Conta([titular_1, titular_2], '001', '0256')
minha_conta.depositar(1000)
minha_conta.sacar(500)
minha_conta.extrato()
banco_delas.add_conta(minha_conta)


    





