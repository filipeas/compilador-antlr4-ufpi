# Generated from /Users/filipealvessampaio/Documents/UFPI/compiladores/trabalho_final/gramatica.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from gen.gramaticaParser import gramaticaParser
else:
    from gen.gramaticaParser import gramaticaParser
from jasminGenerator import Generator, Id
from Erros import ErroTipoIncompativelDecl, ErroTipoInesperado, ErroTipoNaoInformado, ErroBreak, ErroDeclaracaoJaFeita, \
    ErroVariavelNaoDeclarada, ErroTipoExpressao, ErroTipoExpressaoDiferenteDeIncremento, ErroRetorno, \
    ErroDuplaExpressao, ErroArgumentoEsperado, ErroDeclaracaoDepoisDoBloco


# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # tabela de simbolos // refatorar: usar só uma, se nao da problema no gerador
    tabelaDeSimbolos = {}
    tabelaDeSimbolos_copy = {}

    # bloco de pilha
    blocoDePilha = []

    # argumentos de funcoes
    argumentoDeFuncoes = {}

    # bloco de funcoes com retorno tipado
    blocoRetorno = []

    # controla escopo da execucao: true para escopo local e false para escopo global
    controle_escopo = False
    # controla o endereço de instancia de nova variavel
    controle_endereco_novo = 0

    # flag para controlar se entrou em um calculo de expressao e impedir que jasmin duplique escrita no .j
    controleCalculoExpr = False

    def __init__(self, filename):
        self.jasmin = Generator(filename, self.tabelaDeSimbolos)
        self.label_id = 0

    # Enter a parse tree produced by gramaticaParser#prog.
    def enterProg(self, ctx:gramaticaParser.ProgContext):
        print("Iniciando análise semântica")
        pass

    # Exit a parse tree produced by gramaticaParser#prog.
    def exitProg(self, ctx:gramaticaParser.ProgContext):
        print("Finalizando análise semântica")
        pass


    # Enter a parse tree produced by gramaticaParser#main.
    def enterMain(self, ctx:gramaticaParser.MainContext):
        self.jasmin.enter_main()
        self.controle_escopo = True
        self.blocoDePilha.append('function')
        pass

    # Exit a parse tree produced by gramaticaParser#main.
    def exitMain(self, ctx:gramaticaParser.MainContext):
        self.jasmin.exit_main()
        self.blocoDePilha.pop()
        self.controle_escopo = False
        pass


    # Enter a parse tree produced by gramaticaParser#bloco.
    def enterBloco(self, ctx:gramaticaParser.BlocoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#bloco.
    def exitBloco(self, ctx:gramaticaParser.BlocoContext):
        pass

    # Enter a parse tree produced by gramaticaParser#blocoFuncs.
    def enterBlocoFuncs(self, ctx:gramaticaParser.BlocoFuncsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#blocoFuncs.
    def exitBlocoFuncs(self, ctx:gramaticaParser.BlocoFuncsContext):
        pass

    # Enter a parse tree produced by gramaticaParser#declaraVariaveis.
    def enterDeclaraVariaveis(self, ctx:gramaticaParser.DeclaraVariaveisContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaraVariaveis.
    def exitDeclaraVariaveis(self, ctx:gramaticaParser.DeclaraVariaveisContext):
        for token in ctx.ID():
            if ctx.TIPO().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, token.getText())

            # se variavel existe e esta no escopo local, da erro
            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, token.getText())

            # se a variavel ja estiver em escopo global, guarda ela para recuperar na saida da funcao de escopo local
            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == False:
                self.tabelaDeSimbolos_copy[token.getText()] = self.tabelaDeSimbolos[token.getText()]

            self.tabelaDeSimbolos[token.getText()] = Id(type=ctx.TIPO().getText(), scope=self.controle_escopo, address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1 # atualiza o proximo endereco disponivel
            self.jasmin.create(token.getText(), ctx.TIPO().getText(), self.controle_escopo, False, 0)
        pass

    # Enter a parse tree produced by gramaticaParser#declaraConstantes.
    def enterDeclaraConstantes(self, ctx:gramaticaParser.DeclaraConstantesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaraConstantes.
    def exitDeclaraConstantes(self, ctx:gramaticaParser.DeclaraConstantesContext):
        for key, token in enumerate(ctx.ID()):
            if ctx.TIPO().getText() == '<missing <INVALID>>':
                raise ErroTipoNaoInformado(ctx.start.line, token.getText())

            # se variavel existe e esta no escopo local, da erro
            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, token.getText())

            if token.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[token.getText()].scope == False:
                self.tabelaDeSimbolos_copy[token.getText()] = self.tabelaDeSimbolos[token.getText()]

            self.tabelaDeSimbolos[token.getText()] = Id(type=ctx.TIPO().getText(), scope=self.controle_escopo,
                                                        address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1  # atualiza o proximo endereco disponivel
            self.jasmin.create(token.getText(), ctx.TIPO().getText(), self.controle_escopo, True, ctx.op.text)

            # verificar se o tipo atribuido da constante condiz com o valor inserido
            if ctx.TIPO().getText() == 'int' and not ctx.INT():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.TIPO().getText())
            elif ctx.TIPO().getText() == 'real' and not ctx.REAL():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.TIPO().getText())
            elif ctx.TIPO().getText() == 'bool' and not ctx.BOOL():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.TIPO().getText())
            elif ctx.TIPO().getText() == 'String' and not ctx.STRING():
                raise ErroTipoIncompativelDecl(ctx.start.line, ctx.TIPO().getText())
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_com_tipo_e_vazio.
    def enterFuncao_com_tipo_e_vazio(self, ctx:gramaticaParser.Funcao_com_tipo_e_vazioContext):
        self.controle_escopo = True
        self.blocoDePilha.append('function')
        functionId = ctx.ID(0).getText()

        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.TIPO()):
            functionType = ctx.TIPO(0).getText()
        else:
            functionType = None

        if functionId in self.tabelaDeSimbolos:
            raise ErroDeclaracaoJaFeita(ctx.start.line, functionId)

        self.tabelaDeSimbolos[functionId] = Id(type=functionType, scope=False, address=self.controle_endereco_novo)

        self.controle_endereco_novo += 1

        # verificando parametros da funcao
        args = []
        argsNames = []
        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.TIPO()):
            lista = list(zip(ctx.ID()[1:], ctx.TIPO()[1:]))
        else:
            lista = list(zip(ctx.ID()[1:], ctx.TIPO()[0:]))

        for id, tipo in lista:
            # se variavel existe e esta no escopo local, da erro
            if id in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id].scope == self.controle_escopo:
                raise ErroDeclaracaoJaFeita(ctx.start.line, id.getText())

            # se a variavel ja estiver em escopo global, guarda ela para recuperar na saida da funcao de escopo local
            if id.getText() in self.tabelaDeSimbolos and self.tabelaDeSimbolos[id.getText()].scope == False:
                self.tabelaDeSimbolos_copy[id.getText()] = self.tabelaDeSimbolos[id.getText()]

            self.tabelaDeSimbolos[id.getText()] = Id(type=tipo.getText(), scope=self.controle_escopo, address=self.controle_endereco_novo)
            self.controle_endereco_novo += 1
            args.append(tipo.getText())
            argsNames.append(id.getText())

        self.argumentoDeFuncoes[functionId] = args
        self.jasmin.enter_function(functionId, argsNames)

        # se a funcao tem retorno de tipo entao deve verificar se tem funcao de retorno no bloco
        if len(ctx.ID()) <= len(ctx.TIPO()):
            self.blocoRetorno.append(functionType)
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_com_tipo_e_vazio.
    def exitFuncao_com_tipo_e_vazio(self, ctx:gramaticaParser.Funcao_com_tipo_e_vazioContext):
        if len(self.blocoRetorno) > 0:
            self.blocoRetorno.pop()

        if len(self.blocoRetorno) > 0:
            raise ErroRetorno(ctx.start.line)

        self.jasmin.exit_function()

        self.blocoDePilha.pop()

        for item in list(self.tabelaDeSimbolos):
            if self.tabelaDeSimbolos[item].scope:
                del self.tabelaDeSimbolos[item]

        for item in self.tabelaDeSimbolos_copy:
            self.tabelaDeSimbolos[item] = self.tabelaDeSimbolos_copy[item]

        # teste
        for item in self.tabelaDeSimbolos:
            print(item, ' => ', self.tabelaDeSimbolos[item].scope)
        print('----------')

        self.controle_escopo = False
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_for.
    def enterFuncao_for(self, ctx:gramaticaParser.Funcao_forContext):
        # verificando primeiro parametro do for
        ctxId = ctx.ID(0).getText()
        # se variavel ja foi declarada, da erro
        if ctxId not in self.tabelaDeSimbolos:
            raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)
        # se declaracao nao for do tipo int, da erro
        if self.controle_escopo:
            if self.tabelaDeSimbolos[ctxId].type != 'int':
                raise ErroTipoInesperado(ctx.start.line, 'int', self.tabelaDeSimbolos[ctxId].type)

        # verifica se ID declarado é igual aos ids do incremento
        if ctxId != ctx.incremento().ID()[0].getText() or ctxId != ctx.incremento().ID()[1].getText():
            raise ErroTipoExpressaoDiferenteDeIncremento(ctx.start.line)

        if ctx.ID(1) == None:
            ctxInt = ctx.INT()
            # print(ctxInt, self.tabelaDeSimbolos)
            self.jasmin.enter_for_com_valor(ctxInt, ctxId, ctx.funcao_break() != None, self.controle_escopo)
        else:
            ctxInt = self.tabelaDeSimbolos[ctx.ID(1).getText()].address
            # print(ctxInt, self.tabelaDeSimbolos)
            self.jasmin.enter_for(ctxInt, ctxId, ctx.funcao_break() != None, self.controle_escopo)

        ctx.stack_idx = len(self.blocoDePilha)

        # empilha flag loop para saber se entrou no loop
        self.blocoDePilha.append('loop')
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_for.
    def exitFuncao_for(self, ctx:gramaticaParser.Funcao_forContext):
        # desempilha flag loop para saber se saiu do loop
        self.blocoDePilha.pop()

        ctxId = ctx.ID(0).getText()

        # print(ctxId)
        # print(ctx.expressao().val)
        # print(ctx.expressao().inh)
        # print(ctx.stack_idx)
        # print(ctx.incremento().op.text, ctx.incremento().INT())
        # print(ctx.funcao_break() == None)

        # ctxInt = self.tabelaDeSimbolos[ctx.ID(1).getText()].address
        # print(ctxInt, self.tabelaDeSimbolos)
        self.jasmin.exit_for(ctxId, ctx.expressao().val, ctx.incremento().op.text, ctx.incremento().INT(), self.controle_escopo)
        pass


    # Enter a parse tree produced by gramaticaParser#incremento.
    def enterIncremento(self, ctx:gramaticaParser.IncrementoContext):
        # FALTA TERMINAR
        pass

    # Exit a parse tree produced by gramaticaParser#incremento.
    def exitIncremento(self, ctx:gramaticaParser.IncrementoContext):
        # FALTA TERMINAR
        # print(ctx.op.text, ctx.INT())
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_or.
    def enterOperacao_or(self, ctx:gramaticaParser.Operacao_orContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_or.
    def exitOperacao_or(self, ctx:gramaticaParser.Operacao_orContext):
        if ctx.expressao().type != 'bool':
            raise ErroTipoExpressao(ctx.start.line, '||', ctx.expressao().type)
        elif ctx.termo().type != 'bool':
            raise ErroTipoExpressao(ctx.start.line, '||', ctx.termo().type)
        else:
            ctx.type = 'bool'

        ctx.val = self.jasmin.calc_or(ctx.expressao().val, ctx.termo().val, self.controle_endereco_novo)
        self.controle_endereco_novo += 1

        if ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.termo().val + 1))
        elif ctx.inh_type == 'if':
            ctx.end_label = self.jasmin.enter_if(ctx.termo().val + 1)
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo.
    def enterVai_termo(self, ctx:gramaticaParser.Vai_termoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo.
    def exitVai_termo(self, ctx:gramaticaParser.Vai_termoContext):
        ctx.type = ctx.termo().type
        ctx.val = ctx.termo().val

        if ctx.inh_type == 'for':
            self.jasmin.store_var(ctx.inh, ctx.val)
        elif ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.val))
        elif ctx.inh_type == 'if':
            ctx.end_label = self.jasmin.enter_if(ctx.val)
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_and.
    def enterOperacao_and(self, ctx:gramaticaParser.Operacao_andContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_and.
    def exitOperacao_and(self, ctx:gramaticaParser.Operacao_andContext):
        if ctx.termo().type != 'bool':
            raise ErroTipoExpressao(ctx.start.line, '&&', ctx.termo().type)
        elif ctx.termo2().type != 'bool':
            raise ErroTipoExpressao(ctx.start.line, '&&', ctx.termo2().type)
        else:
            ctx.type = 'bool'

        ctx.val = self.jasmin.calc_and(ctx.termo().val, ctx.termo2().val, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo2.
    def enterVai_termo2(self, ctx:gramaticaParser.Vai_termo2Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo2.
    def exitVai_termo2(self, ctx:gramaticaParser.Vai_termo2Context):
        ctx.type = ctx.termo2().type
        ctx.val = ctx.termo2().val
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_comparacao.
    def enterOperacao_comparacao(self, ctx:gramaticaParser.Operacao_comparacaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_comparacao.
    def exitOperacao_comparacao(self, ctx:gramaticaParser.Operacao_comparacaoContext):
        termo2Type = ctx.termo2().type
        termo2Val = ctx.termo2().val  # endereco de variavel temporario

        termo3Type = ctx.termo3().type
        termo3Val = ctx.termo3().val  # endereco de variavel temporario

        if str(termo2Type) != str(termo3Type):
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo2Type, termo3Type)

        ctx.type = 'bool'
        ctx.val = self.jasmin.calc_eq(termo2Type, termo2Val, termo3Val, self.controle_endereco_novo, ctx.op.text)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo3.
    def enterVai_termo3(self, ctx:gramaticaParser.Vai_termo3Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo3.
    def exitVai_termo3(self, ctx:gramaticaParser.Vai_termo3Context):
        ctx.type = ctx.termo3().type
        ctx.val = ctx.termo3().val
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo4.
    def enterVai_termo4(self, ctx:gramaticaParser.Vai_termo4Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo4.
    def exitVai_termo4(self, ctx:gramaticaParser.Vai_termo4Context):
        ctx.type = ctx.termo4().type
        ctx.val = ctx.termo4().val
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_igual_dif.
    def enterOperacao_igual_dif(self, ctx:gramaticaParser.Operacao_igual_difContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_igual_dif.
    def exitOperacao_igual_dif(self, ctx:gramaticaParser.Operacao_igual_difContext):
        termo3Type = ctx.termo3().type
        termo3Val = ctx.termo3().val  # endereco de variavel temporario

        termo4Type = ctx.termo4().type
        termo4Val = ctx.termo4().val  # endereco de variavel temporario

        if str(termo3Type) != str(termo4Type):
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo3Type, termo4Type)

        ctx.type = 'bool'
        ctx.val = self.jasmin.calc_eq(termo3Type, termo3Val, termo4Val, self.controle_endereco_novo, ctx.op.text)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo5.
    def enterVai_termo5(self, ctx:gramaticaParser.Vai_termo5Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo5.
    def exitVai_termo5(self, ctx:gramaticaParser.Vai_termo5Context):
        ctx.type = ctx.termo5().type
        ctx.val = ctx.termo5().val
        pass

    # Enter a parse tree produced by gramaticaParser#vai_termo6.
    def enterVai_termo6(self, ctx: gramaticaParser.Vai_termo6Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo6.
    def exitVai_termo6(self, ctx: gramaticaParser.Vai_termo6Context):
        ctx.type = ctx.termo6().type
        ctx.val = ctx.termo6().val
        pass

    # Enter a parse tree produced by gramaticaParser#operacao_menos_not.
    def enterOperacao_menos_not(self, ctx: gramaticaParser.Operacao_menos_notContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_menos_not.
    def exitOperacao_menos_not(self, ctx: gramaticaParser.Operacao_menos_notContext):
        if ctx.op.text == '-':
            if (ctx.termo6().type == 'real') or (ctx.termo6().type == 'int'):
                ctx.type = ctx.termo6().type
            else:
                raise ErroTipoExpressao(ctx.start.line, ctx.op.text, ctx.termo6().type)

            ctx.val = self.jasmin.calc_minus(ctx.termo6().type, ctx.termo6().val, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        elif ctx.op.text == '!':
            if ctx.termo6().type == 'bool':
                ctx.type = 'bool'
            else:
                raise ErroTipoExpressao(ctx.start.line, ctx.op.text, ctx.termo6().type)

            ctx.val = self.jasmin.calc_not(ctx.termo6().val, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        pass

    # Enter a parse tree produced by gramaticaParser#operacao_soma_sub.
    def enterOperacao_soma_sub(self, ctx:gramaticaParser.Operacao_soma_subContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_soma_sub.
    def exitOperacao_soma_sub(self, ctx:gramaticaParser.Operacao_soma_subContext):
        termo4Type = ctx.termo4().type
        termo4Val = ctx.termo4().val # endereco de variavel temporario

        termo5Type = ctx.termo5().type
        termo5Val = ctx.termo5().val # endereco de variavel temporario

        if not ((termo4Type == 'int') or (termo4Type == 'real')): # se termo4 nao for int ou real é pra dar erro
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo4Type)
        elif not ((termo5Type == 'int') or (termo5Type == 'real')): # se termo5 nao for int ou real é pra dar erro
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo5Type)
        elif termo4Type == 'real' and termo5Type == 'real':
            ctx.type = 'real'
            val1, val2 = termo4Val, termo5Val
        elif termo4Type == 'real':
            ctx.type = 'real'
            val1, val2 = termo4Val, self.jasmin.int_to_float(termo5Val)
        elif termo5Type == 'real':
            ctx.type = 'real'
            val1, val2 = self.jasmin.int_to_float(termo4Val), termo5Val
        else:
            ctx.type = 'int'
            val1, val2 = termo4Val, termo5Val

        if ctx.op.text == '+':
            ctx.val = self.jasmin.add(ctx.type, val1, val2, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        else:
            ctx.val = self.jasmin.sub(ctx.type, val1, val2, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#vai_fator.
    def enterVai_fator(self, ctx:gramaticaParser.Vai_fatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_fator.
    def exitVai_fator(self, ctx:gramaticaParser.Vai_fatorContext):
        ctx.type = ctx.fator().type
        ctx.val = ctx.fator().val
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_multi_div.
    def enterOperacao_multi_div(self, ctx:gramaticaParser.Operacao_multi_divContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_multi_div.
    def exitOperacao_multi_div(self, ctx:gramaticaParser.Operacao_multi_divContext):
        termo5Type = ctx.termo5().type
        termo5Val = ctx.termo5().val  # endereco de variavel temporario

        termo6Type = ctx.termo6().type
        termo6Val = ctx.termo6().val  # endereco de variavel temporario

        if not ((termo5Type == 'int') or (termo5Type == 'real')):  # se termo5 nao for int ou real é pra dar erro
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo5Type)
        elif not ((termo6Type == 'int') or (termo6Type == 'real')):  # se termo6 nao for int ou real é pra dar erro
            raise ErroTipoExpressao(ctx.start.line, ctx.op.text, termo6Type)
        elif termo5Type == 'real' and termo6Type == 'real':
            ctx.type = 'real'
            val1, val2 = termo5Val, termo6Val
        elif termo5Type == 'real':
            ctx.type = 'real'
            val1, val2 = termo5Val, self.jasmin.int_to_float(termo6Val)
        elif termo6Type == 'real':
            ctx.type = 'real'
            val1, val2 = self.jasmin.int_to_float(termo5Val), termo6Val
        else:
            ctx.type = 'int'
            val1, val2 = termo5Val, termo6Val

        if ctx.op.text == '*':
            ctx.val = self.jasmin.mul(ctx.type, val1, val2, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        else:
            ctx.val = self.jasmin.div(ctx.type, val1, val2, self.controle_endereco_novo)
            self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_abre_fecha_expressao.
    def enterTerminal_abre_fecha_expressao(self, ctx:gramaticaParser.Terminal_abre_fecha_expressaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_abre_fecha_expressao.
    def exitTerminal_abre_fecha_expressao(self, ctx:gramaticaParser.Terminal_abre_fecha_expressaoContext):
        ctx.type = ctx.expressao().type
        ctx.val = ctx.expressao().val
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_id.
    def enterTerminal_id(self, ctx:gramaticaParser.Terminal_idContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_id.
    def exitTerminal_id(self, ctx:gramaticaParser.Terminal_idContext):
        ctxId = ctx.ID().getText()
        if ctxId not in self.tabelaDeSimbolos:
            raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)

        ctx.type = self.tabelaDeSimbolos[ctxId].type
        ctx.val = self.jasmin.load_var(ctxId, self.controle_escopo, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_int.
    def enterTerminal_int(self, ctx:gramaticaParser.Terminal_intContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_int.
    def exitTerminal_int(self, ctx:gramaticaParser.Terminal_intContext):
        ctx.type = 'int'
        ctx.val = self.controle_endereco_novo # guarda endereco para realizar leitura
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_float.
    def enterTerminal_float(self, ctx:gramaticaParser.Terminal_floatContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_float.
    def exitTerminal_float(self, ctx:gramaticaParser.Terminal_floatContext):
        ctx.type = 'real'
        ctx.val = self.controle_endereco_novo
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_string.
    def enterTerminal_string(self, ctx:gramaticaParser.Terminal_stringContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_string.
    def exitTerminal_string(self, ctx:gramaticaParser.Terminal_stringContext):
        ctx.type = 'String'
        ctx.val = self.controle_endereco_novo
        self.jasmin.create_temp(ctx.getText(), ctx.type, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_boolean.
    def enterTerminal_boolean(self, ctx:gramaticaParser.Terminal_booleanContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_boolean.
    def exitTerminal_boolean(self, ctx:gramaticaParser.Terminal_booleanContext):
        ctx.type = 'bool'
        ctx.val = self.controle_endereco_novo
        self.jasmin.create_temp(0 if ctx.getText() == 'false' else 1, ctx.type, self.controle_endereco_novo)
        self.controle_endereco_novo += 1
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_funcao_chamada.
    def enterTerminal_funcao_chamada(self, ctx:gramaticaParser.Terminal_funcao_chamadaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_funcao_chamada.
    def exitTerminal_funcao_chamada(self, ctx:gramaticaParser.Terminal_funcao_chamadaContext):
        ctx.type = ctx.funcao_chamada().type
        ctx.val = ctx.funcao_chamada().val
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_while.
    def enterFuncao_while(self, ctx:gramaticaParser.Funcao_whileContext):
        ctx.expressao().inh_type = 'while'
        ctx.expressao().inh = self.jasmin.enter_while(len(self.blocoDePilha))
        self.controle_endereco_novo += 1

        # empilha flag loop para saber se entrou no loop
        self.blocoDePilha.append('loop')
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_while.
    def exitFuncao_while(self, ctx:gramaticaParser.Funcao_whileContext):
        if ctx.expressao().type != 'bool':
            raise ErroTipoInesperado(ctx.start.line, 'bool', ctx.expressao().type)

        # desempilha flag loop para saber se saiu do loop
        self.blocoDePilha.pop()
        self.jasmin.exit_while(len(self.blocoDePilha))
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_if.
    def enterFuncao_if(self, ctx:gramaticaParser.Funcao_ifContext):
        ctx.expressao().inh_type = 'if'
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_if.
    def exitFuncao_if(self, ctx:gramaticaParser.Funcao_ifContext):
        if ctx.expressao().type != 'bool':
            raise ErroTipoInesperado(ctx.start.line, 'bool', ctx.expressao().type)
        if ctx.funcao_else() != None:
            self.jasmin.make_label('end_else_' + str(ctx.expressao().end_label))
        else:
            self.jasmin.make_label('if_' + str(ctx.expressao().end_label))
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_else.
    def enterFuncao_else(self, ctx:gramaticaParser.Funcao_elseContext):
        self.jasmin.enter_else()
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_else.
    def exitFuncao_else(self, ctx:gramaticaParser.Funcao_elseContext):
        # self.jasmin.make_label('else_')
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_break.
    def enterFuncao_break(self, ctx:gramaticaParser.Funcao_breakContext):
        if 'loop' not in self.blocoDePilha:
            raise ErroBreak(ctx.start.line)
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_break.
    def exitFuncao_break(self, ctx:gramaticaParser.Funcao_breakContext):
        # print(ctx.funcao_for)
        # self.jasmin.break_loop(len(self.blocoDePilha) - 1)
        pass


    # Enter a parse tree produced by gramaticaParser#assignment_print.
    def enterAssignment_print(self, ctx:gramaticaParser.Assignment_printContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment_print.
    def exitAssignment_print(self, ctx:gramaticaParser.Assignment_printContext):
        type_val = []
        for expr in ctx.expressao():
            type_val.append((expr.type, expr.val))

        self.jasmin.print(type_val)
        pass


    # Enter a parse tree produced by gramaticaParser#assignment_input.
    def enterAssignment_input(self, ctx:gramaticaParser.Assignment_inputContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment_input.
    def exitAssignment_input(self, ctx:gramaticaParser.Assignment_inputContext):
        for var in ctx.ID():
            ctxId = var.getText()
            if ctxId not in self.tabelaDeSimbolos:
                raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)
            self.jasmin.input(ctxId, self.controle_escopo)
        pass


    # Enter a parse tree produced by gramaticaParser#expressao_atrib.
    def enterExpressao_atrib(self, ctx:gramaticaParser.Expressao_atribContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expressao_atrib.
    def exitExpressao_atrib(self, ctx:gramaticaParser.Expressao_atribContext):
        ctxId = ctx.ID().getText()
        ctxVal = ctx.expressao().val
        variable = self.tabelaDeSimbolos[ctxId]

        if ctxId not in self.tabelaDeSimbolos:
            raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)

        if self.controle_escopo:
            expected = variable.type
            received = ctx.expressao().type

            # casting para que a variavel que vai receber use o tipo calculado da expressao
            # o tipo calculado da expressao é baseado no tipo dos numeros da expressao, e nao é considerado os operadores
            # ex: (2 + 2) / 2 vai ser expressao int, pq todos os numeros sao inteiros
            # ex: (2 + 2) / 2.0 vai ser expressao real, pq pelo menos 1 numero é real
            self.jasmin.tabela_simbolo[ctxId].type = ctx.expressao().type
            if (expected == 'int' and received == 'real') or (expected == 'real' and received == 'int'):
                expected = 'real'
                received = 'real'

            if expected != received:
                raise ErroTipoInesperado(ctx.start.line, expected, received)

            self.jasmin.store_var(ctxId, ctxVal, variable.address, self.controle_escopo)
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_chamada.
    def enterFuncao_chamada(self, ctx:gramaticaParser.Funcao_chamadaContext):
        ctxId = ctx.ID().getText()
        if ctxId not in self.tabelaDeSimbolos:
            raise ErroVariavelNaoDeclarada(ctx.start.line, ctxId)
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_chamada.
    def exitFuncao_chamada(self, ctx:gramaticaParser.Funcao_chamadaContext):
        functionId = ctx.ID().getText()

        if len(self.argumentoDeFuncoes[functionId]) != len(ctx.expressao()):
            raise ErroArgumentoEsperado(ctx.start.line, len(self.argumentoDeFuncoes[functionId]), len(ctx.expressao()))

        for expected, recieved in list(zip(self.argumentoDeFuncoes[functionId], ctx.expressao())):
            if expected != recieved.type:
                raise ErroTipoInesperado(ctx.start.line, expected, recieved.type)

        ctx.type = self.tabelaDeSimbolos[functionId].type

        args = []
        types = []
        for exp in ctx.expressao():
            args.append(exp.val)
            types.append(exp.type)
        ctx.val = self.jasmin.function_call(functionId, args, types)
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_retorno.
    def enterFuncao_retorno(self, ctx:gramaticaParser.Funcao_retornoContext):
        if 'function' not in self.blocoDePilha:
            raise ErroRetorno(ctx.start.line)
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_retorno.
    def exitFuncao_retorno(self, ctx:gramaticaParser.Funcao_retornoContext):
        if ctx.expressao().type and len(self.blocoRetorno) == 0:
            raise ErroRetorno(ctx.start.line)

        if self.blocoRetorno[0] != ctx.expressao().type:
            raise ErroTipoInesperado(ctx.start.line, self.blocoRetorno[0], ctx.expressao().type)

        self.jasmin.do_return(ctx.expressao().val, self.blocoRetorno[0])
        pass



del gramaticaParser