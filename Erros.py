class ErroVariavelNaoDeclarada(Exception):
    def __init__(self, line, id):
        mensagem = 'Linha {}: ID não foi declarado: {}'.format(line, id)
        super().__init__(mensagem)

class ErroDeclaracaoJaFeita(Exception):
    def __init__(self, line, id):
        mensagem = 'Linha {}: ID já declarado: {}'.format(line, id)
        super().__init__(mensagem)

class ErroTipoNaoInformado(Exception):
    def __init__(self, line, id):
        mensagem = 'Linha {}: Tipo não informado: {}'.format(line, id)
        super().__init__(mensagem)

class ErroTipoInesperado(Exception):
    def __init__(self, line, receivedType):
        mensagem = 'Linha {}: Esperado o tipo int ou real mas foi recebido o tipo {}'.format(line, receivedType)
        super().__init__(mensagem)

class ErroTipoIncompativelDecl(Exception):
    def __init__(self, line, type):
        mensagem = 'Linha {}: Esperado o tipo {} na declaração da constante'.format(line, type)
        super().__init__(mensagem)

class ErroBreak(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Break fora do loop'.format(line)
        super().__init__(mensagem)

class ErroTipoExpressao(Exception):
    def __init__(self, line, operation, type1, type2=None):
        mensagem = 'Linha {}: Operação {} não suportada para os tipos: {} e {}'.format(line, operation, type1, type2) if type2 else 'Linha {}: Operação {} não suportada para o tipo: {}'.format(line, operation, type1)
        super().__init__(mensagem)

class ErroTipoExpressaoDiferenteDeIncremento(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Variaveis diferentes na declaracao do for e no incremento'.format(line)
        super().__init__(mensagem)

class ErroRetorno(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Retorno fora do escopo da função'.format(line)
        super().__init__(mensagem)

class ErroTipoInesperado(Exception):
    def __init__(self, line, expected_type, received_type):
        mensagem = 'Linha {}: Esperado tipo {}, mas foi recebido {}'.format(line, expected_type, received_type)
        super().__init__(mensagem)

class ErroDuplaExpressao(Exception):
    def __init__(self, line):
        mensagem = 'Linha {}: Expressão possui mais comparadores do que atributos'.format(line)
        super().__init__(mensagem)

class ErroArgumentoEsperado(Exception):
    def __init__(self, line, expectedArgs, recivedArgs):
        mensagem = 'Linha {}: Esperado {} argumentos, mas somente foram recebidos {}'.format(line, expectedArgs, recivedArgs)
        super().__init__(mensagem)

class ErroVariavelNaoEncontradaNaTabelaDeSimbolo(Exception):
    def __init__(self, var_name, escopo):
        mensagem = 'Variavel {} nao encontrada no escopo {}'.format(var_name, 'LOCAL' if escopo else 'GLOBAL')
        super().__init__(mensagem)

class ErroDeclaracaoDepoisDoBloco(Exception):
    def __init__(self):
        mensagem = 'Variaveis declaradas depois do inicio da funcao'
        super().__init__(mensagem)