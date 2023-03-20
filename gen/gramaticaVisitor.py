# Generated from /Users/filipealvessampaio/Documents/UFPI/compiladores/trabalho_final/gramatica.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#main.
    def visitMain(self, ctx:gramaticaParser.MainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#bloco.
    def visitBloco(self, ctx:gramaticaParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#blocoFuncs.
    def visitBlocoFuncs(self, ctx:gramaticaParser.BlocoFuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declaraVariaveis.
    def visitDeclaraVariaveis(self, ctx:gramaticaParser.DeclaraVariaveisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declaraConstantes.
    def visitDeclaraConstantes(self, ctx:gramaticaParser.DeclaraConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_com_tipo_e_vazio.
    def visitFuncao_com_tipo_e_vazio(self, ctx:gramaticaParser.Funcao_com_tipo_e_vazioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_for.
    def visitFuncao_for(self, ctx:gramaticaParser.Funcao_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#incremento.
    def visitIncremento(self, ctx:gramaticaParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_or.
    def visitOperacao_or(self, ctx:gramaticaParser.Operacao_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo.
    def visitVai_termo(self, ctx:gramaticaParser.Vai_termoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_and.
    def visitOperacao_and(self, ctx:gramaticaParser.Operacao_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo2.
    def visitVai_termo2(self, ctx:gramaticaParser.Vai_termo2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_comparacao.
    def visitOperacao_comparacao(self, ctx:gramaticaParser.Operacao_comparacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo3.
    def visitVai_termo3(self, ctx:gramaticaParser.Vai_termo3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo4.
    def visitVai_termo4(self, ctx:gramaticaParser.Vai_termo4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_igual_dif.
    def visitOperacao_igual_dif(self, ctx:gramaticaParser.Operacao_igual_difContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo5.
    def visitVai_termo5(self, ctx:gramaticaParser.Vai_termo5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_soma_sub.
    def visitOperacao_soma_sub(self, ctx:gramaticaParser.Operacao_soma_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_multi_div.
    def visitOperacao_multi_div(self, ctx:gramaticaParser.Operacao_multi_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_termo6.
    def visitVai_termo6(self, ctx:gramaticaParser.Vai_termo6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#operacao_menos_not.
    def visitOperacao_menos_not(self, ctx:gramaticaParser.Operacao_menos_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#vai_fator.
    def visitVai_fator(self, ctx:gramaticaParser.Vai_fatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_abre_fecha_expressao.
    def visitTerminal_abre_fecha_expressao(self, ctx:gramaticaParser.Terminal_abre_fecha_expressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_id.
    def visitTerminal_id(self, ctx:gramaticaParser.Terminal_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_int.
    def visitTerminal_int(self, ctx:gramaticaParser.Terminal_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_float.
    def visitTerminal_float(self, ctx:gramaticaParser.Terminal_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_string.
    def visitTerminal_string(self, ctx:gramaticaParser.Terminal_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_boolean.
    def visitTerminal_boolean(self, ctx:gramaticaParser.Terminal_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#terminal_funcao_chamada.
    def visitTerminal_funcao_chamada(self, ctx:gramaticaParser.Terminal_funcao_chamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_while.
    def visitFuncao_while(self, ctx:gramaticaParser.Funcao_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_if.
    def visitFuncao_if(self, ctx:gramaticaParser.Funcao_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_else.
    def visitFuncao_else(self, ctx:gramaticaParser.Funcao_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_break.
    def visitFuncao_break(self, ctx:gramaticaParser.Funcao_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment_print.
    def visitAssignment_print(self, ctx:gramaticaParser.Assignment_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment_input.
    def visitAssignment_input(self, ctx:gramaticaParser.Assignment_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expressao_atrib.
    def visitExpressao_atrib(self, ctx:gramaticaParser.Expressao_atribContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_chamada.
    def visitFuncao_chamada(self, ctx:gramaticaParser.Funcao_chamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#funcao_retorno.
    def visitFuncao_retorno(self, ctx:gramaticaParser.Funcao_retornoContext):
        return self.visitChildren(ctx)



del gramaticaParser