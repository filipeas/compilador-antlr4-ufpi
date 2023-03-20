# Generated from /Users/filipealvessampaio/Documents/UFPI/compiladores/trabalho_final/gramatica.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#prog.
    def enterProg(self, ctx:gramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by gramaticaParser#prog.
    def exitProg(self, ctx:gramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by gramaticaParser#main.
    def enterMain(self, ctx:gramaticaParser.MainContext):
        pass

    # Exit a parse tree produced by gramaticaParser#main.
    def exitMain(self, ctx:gramaticaParser.MainContext):
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
        pass


    # Enter a parse tree produced by gramaticaParser#declaraConstantes.
    def enterDeclaraConstantes(self, ctx:gramaticaParser.DeclaraConstantesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaraConstantes.
    def exitDeclaraConstantes(self, ctx:gramaticaParser.DeclaraConstantesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_com_tipo_e_vazio.
    def enterFuncao_com_tipo_e_vazio(self, ctx:gramaticaParser.Funcao_com_tipo_e_vazioContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_com_tipo_e_vazio.
    def exitFuncao_com_tipo_e_vazio(self, ctx:gramaticaParser.Funcao_com_tipo_e_vazioContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_for.
    def enterFuncao_for(self, ctx:gramaticaParser.Funcao_forContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_for.
    def exitFuncao_for(self, ctx:gramaticaParser.Funcao_forContext):
        pass


    # Enter a parse tree produced by gramaticaParser#incremento.
    def enterIncremento(self, ctx:gramaticaParser.IncrementoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#incremento.
    def exitIncremento(self, ctx:gramaticaParser.IncrementoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_or.
    def enterOperacao_or(self, ctx:gramaticaParser.Operacao_orContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_or.
    def exitOperacao_or(self, ctx:gramaticaParser.Operacao_orContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo.
    def enterVai_termo(self, ctx:gramaticaParser.Vai_termoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo.
    def exitVai_termo(self, ctx:gramaticaParser.Vai_termoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_and.
    def enterOperacao_and(self, ctx:gramaticaParser.Operacao_andContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_and.
    def exitOperacao_and(self, ctx:gramaticaParser.Operacao_andContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo2.
    def enterVai_termo2(self, ctx:gramaticaParser.Vai_termo2Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo2.
    def exitVai_termo2(self, ctx:gramaticaParser.Vai_termo2Context):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_comparacao.
    def enterOperacao_comparacao(self, ctx:gramaticaParser.Operacao_comparacaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_comparacao.
    def exitOperacao_comparacao(self, ctx:gramaticaParser.Operacao_comparacaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo3.
    def enterVai_termo3(self, ctx:gramaticaParser.Vai_termo3Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo3.
    def exitVai_termo3(self, ctx:gramaticaParser.Vai_termo3Context):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo4.
    def enterVai_termo4(self, ctx:gramaticaParser.Vai_termo4Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo4.
    def exitVai_termo4(self, ctx:gramaticaParser.Vai_termo4Context):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_igual_dif.
    def enterOperacao_igual_dif(self, ctx:gramaticaParser.Operacao_igual_difContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_igual_dif.
    def exitOperacao_igual_dif(self, ctx:gramaticaParser.Operacao_igual_difContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo5.
    def enterVai_termo5(self, ctx:gramaticaParser.Vai_termo5Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo5.
    def exitVai_termo5(self, ctx:gramaticaParser.Vai_termo5Context):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_soma_sub.
    def enterOperacao_soma_sub(self, ctx:gramaticaParser.Operacao_soma_subContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_soma_sub.
    def exitOperacao_soma_sub(self, ctx:gramaticaParser.Operacao_soma_subContext):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_multi_div.
    def enterOperacao_multi_div(self, ctx:gramaticaParser.Operacao_multi_divContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_multi_div.
    def exitOperacao_multi_div(self, ctx:gramaticaParser.Operacao_multi_divContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_termo6.
    def enterVai_termo6(self, ctx:gramaticaParser.Vai_termo6Context):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_termo6.
    def exitVai_termo6(self, ctx:gramaticaParser.Vai_termo6Context):
        pass


    # Enter a parse tree produced by gramaticaParser#operacao_menos_not.
    def enterOperacao_menos_not(self, ctx:gramaticaParser.Operacao_menos_notContext):
        pass

    # Exit a parse tree produced by gramaticaParser#operacao_menos_not.
    def exitOperacao_menos_not(self, ctx:gramaticaParser.Operacao_menos_notContext):
        pass


    # Enter a parse tree produced by gramaticaParser#vai_fator.
    def enterVai_fator(self, ctx:gramaticaParser.Vai_fatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#vai_fator.
    def exitVai_fator(self, ctx:gramaticaParser.Vai_fatorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_abre_fecha_expressao.
    def enterTerminal_abre_fecha_expressao(self, ctx:gramaticaParser.Terminal_abre_fecha_expressaoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_abre_fecha_expressao.
    def exitTerminal_abre_fecha_expressao(self, ctx:gramaticaParser.Terminal_abre_fecha_expressaoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_id.
    def enterTerminal_id(self, ctx:gramaticaParser.Terminal_idContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_id.
    def exitTerminal_id(self, ctx:gramaticaParser.Terminal_idContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_int.
    def enterTerminal_int(self, ctx:gramaticaParser.Terminal_intContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_int.
    def exitTerminal_int(self, ctx:gramaticaParser.Terminal_intContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_float.
    def enterTerminal_float(self, ctx:gramaticaParser.Terminal_floatContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_float.
    def exitTerminal_float(self, ctx:gramaticaParser.Terminal_floatContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_string.
    def enterTerminal_string(self, ctx:gramaticaParser.Terminal_stringContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_string.
    def exitTerminal_string(self, ctx:gramaticaParser.Terminal_stringContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_boolean.
    def enterTerminal_boolean(self, ctx:gramaticaParser.Terminal_booleanContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_boolean.
    def exitTerminal_boolean(self, ctx:gramaticaParser.Terminal_booleanContext):
        pass


    # Enter a parse tree produced by gramaticaParser#terminal_funcao_chamada.
    def enterTerminal_funcao_chamada(self, ctx:gramaticaParser.Terminal_funcao_chamadaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#terminal_funcao_chamada.
    def exitTerminal_funcao_chamada(self, ctx:gramaticaParser.Terminal_funcao_chamadaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_while.
    def enterFuncao_while(self, ctx:gramaticaParser.Funcao_whileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_while.
    def exitFuncao_while(self, ctx:gramaticaParser.Funcao_whileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_if.
    def enterFuncao_if(self, ctx:gramaticaParser.Funcao_ifContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_if.
    def exitFuncao_if(self, ctx:gramaticaParser.Funcao_ifContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_else.
    def enterFuncao_else(self, ctx:gramaticaParser.Funcao_elseContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_else.
    def exitFuncao_else(self, ctx:gramaticaParser.Funcao_elseContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_break.
    def enterFuncao_break(self, ctx:gramaticaParser.Funcao_breakContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_break.
    def exitFuncao_break(self, ctx:gramaticaParser.Funcao_breakContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment_print.
    def enterAssignment_print(self, ctx:gramaticaParser.Assignment_printContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment_print.
    def exitAssignment_print(self, ctx:gramaticaParser.Assignment_printContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment_input.
    def enterAssignment_input(self, ctx:gramaticaParser.Assignment_inputContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment_input.
    def exitAssignment_input(self, ctx:gramaticaParser.Assignment_inputContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expressao_atrib.
    def enterExpressao_atrib(self, ctx:gramaticaParser.Expressao_atribContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expressao_atrib.
    def exitExpressao_atrib(self, ctx:gramaticaParser.Expressao_atribContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_chamada.
    def enterFuncao_chamada(self, ctx:gramaticaParser.Funcao_chamadaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_chamada.
    def exitFuncao_chamada(self, ctx:gramaticaParser.Funcao_chamadaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#funcao_retorno.
    def enterFuncao_retorno(self, ctx:gramaticaParser.Funcao_retornoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#funcao_retorno.
    def exitFuncao_retorno(self, ctx:gramaticaParser.Funcao_retornoContext):
        pass



del gramaticaParser