# Generated from /Users/filipealvessampaio/Documents/UFPI/compiladores/trabalho_final/gramatica.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,345,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,4,1,4,1,4,1,4,5,4,
        112,8,4,10,4,12,4,115,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,5,4,127,8,4,10,4,12,4,130,9,4,1,4,3,4,133,8,4,1,5,5,5,136,8,5,
        10,5,12,5,139,9,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,148,8,5,10,5,12,
        5,151,9,5,3,5,153,8,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,173,8,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,189,8,8,10,8,12,8,192,9,8,
        1,9,1,9,1,9,1,9,1,9,1,9,5,9,200,8,9,10,9,12,9,203,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,211,8,10,10,10,12,10,214,9,10,1,11,1,11,
        1,11,1,11,1,11,1,11,5,11,222,8,11,10,11,12,11,225,9,11,1,12,1,12,
        1,12,1,12,1,12,1,12,5,12,233,8,12,10,12,12,12,236,9,12,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,244,8,13,10,13,12,13,247,9,13,1,14,1,14,
        1,14,3,14,252,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,3,15,264,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,282,8,17,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,5,20,297,8,20,
        10,20,12,20,300,9,20,3,20,302,8,20,1,20,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,5,21,312,8,21,10,21,12,21,315,9,21,1,21,1,21,1,21,1,22,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,5,23,330,8,23,10,23,
        12,23,333,9,23,3,23,335,8,23,1,23,1,23,1,24,1,24,3,24,341,8,24,1,
        24,1,24,1,24,0,6,16,18,20,22,24,26,25,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,6,3,0,31,31,33,34,36,
        36,1,0,11,12,1,0,15,18,1,0,19,20,1,0,21,22,2,0,12,12,30,30,357,0,
        53,1,0,0,0,2,64,1,0,0,0,4,74,1,0,0,0,6,105,1,0,0,0,8,132,1,0,0,0,
        10,137,1,0,0,0,12,159,1,0,0,0,14,176,1,0,0,0,16,182,1,0,0,0,18,193,
        1,0,0,0,20,204,1,0,0,0,22,215,1,0,0,0,24,226,1,0,0,0,26,237,1,0,
        0,0,28,251,1,0,0,0,30,263,1,0,0,0,32,265,1,0,0,0,34,273,1,0,0,0,
        36,283,1,0,0,0,38,288,1,0,0,0,40,291,1,0,0,0,42,306,1,0,0,0,44,319,
        1,0,0,0,46,324,1,0,0,0,48,338,1,0,0,0,50,52,3,8,4,0,51,50,1,0,0,
        0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,59,1,0,0,0,55,53,
        1,0,0,0,56,58,3,10,5,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,3,2,1,0,63,1,1,0,
        0,0,64,65,5,1,0,0,65,66,5,2,0,0,66,67,5,3,0,0,67,68,5,4,0,0,68,69,
        3,4,2,0,69,70,5,5,0,0,70,3,1,0,0,0,71,73,3,8,4,0,72,71,1,0,0,0,73,
        76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,
        0,77,78,3,6,3,0,78,5,1,0,0,0,79,80,3,12,6,0,80,81,3,6,3,0,81,106,
        1,0,0,0,82,83,3,32,16,0,83,84,3,6,3,0,84,106,1,0,0,0,85,86,3,34,
        17,0,86,87,3,6,3,0,87,106,1,0,0,0,88,89,3,40,20,0,89,90,3,6,3,0,
        90,106,1,0,0,0,91,92,3,42,21,0,92,93,3,6,3,0,93,106,1,0,0,0,94,95,
        3,44,22,0,95,96,3,6,3,0,96,106,1,0,0,0,97,98,3,46,23,0,98,99,5,6,
        0,0,99,100,3,6,3,0,100,106,1,0,0,0,101,102,3,48,24,0,102,103,3,6,
        3,0,103,106,1,0,0,0,104,106,1,0,0,0,105,79,1,0,0,0,105,82,1,0,0,
        0,105,85,1,0,0,0,105,88,1,0,0,0,105,91,1,0,0,0,105,94,1,0,0,0,105,
        97,1,0,0,0,105,101,1,0,0,0,105,104,1,0,0,0,106,7,1,0,0,0,107,108,
        5,29,0,0,108,113,5,37,0,0,109,110,5,7,0,0,110,112,5,37,0,0,111,109,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,
        1,0,0,0,115,113,1,0,0,0,116,133,5,6,0,0,117,118,5,8,0,0,118,119,
        5,29,0,0,119,120,5,37,0,0,120,121,5,9,0,0,121,128,7,0,0,0,122,123,
        5,7,0,0,123,124,5,37,0,0,124,125,5,9,0,0,125,127,7,0,0,0,126,122,
        1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,
        1,0,0,0,130,128,1,0,0,0,131,133,5,6,0,0,132,107,1,0,0,0,132,117,
        1,0,0,0,133,9,1,0,0,0,134,136,5,29,0,0,135,134,1,0,0,0,136,139,1,
        0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,140,1,0,0,0,139,137,1,
        0,0,0,140,141,5,37,0,0,141,152,5,2,0,0,142,143,5,29,0,0,143,149,
        5,37,0,0,144,145,5,7,0,0,145,146,5,29,0,0,146,148,5,37,0,0,147,144,
        1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,153,
        1,0,0,0,151,149,1,0,0,0,152,142,1,0,0,0,152,153,1,0,0,0,153,154,
        1,0,0,0,154,155,5,3,0,0,155,156,5,4,0,0,156,157,3,4,2,0,157,158,
        5,5,0,0,158,11,1,0,0,0,159,160,5,10,0,0,160,161,5,2,0,0,161,162,
        5,37,0,0,162,163,5,9,0,0,163,164,5,33,0,0,164,165,5,6,0,0,165,166,
        3,16,8,0,166,167,5,6,0,0,167,168,3,14,7,0,168,169,5,3,0,0,169,170,
        5,4,0,0,170,172,3,6,3,0,171,173,3,38,19,0,172,171,1,0,0,0,172,173,
        1,0,0,0,173,174,1,0,0,0,174,175,5,5,0,0,175,13,1,0,0,0,176,177,5,
        37,0,0,177,178,5,9,0,0,178,179,5,37,0,0,179,180,7,1,0,0,180,181,
        5,33,0,0,181,15,1,0,0,0,182,183,6,8,-1,0,183,184,3,18,9,0,184,190,
        1,0,0,0,185,186,10,2,0,0,186,187,5,13,0,0,187,189,3,18,9,0,188,185,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,17,1,
        0,0,0,192,190,1,0,0,0,193,194,6,9,-1,0,194,195,3,20,10,0,195,201,
        1,0,0,0,196,197,10,2,0,0,197,198,5,14,0,0,198,200,3,20,10,0,199,
        196,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,
        19,1,0,0,0,203,201,1,0,0,0,204,205,6,10,-1,0,205,206,3,22,11,0,206,
        212,1,0,0,0,207,208,10,2,0,0,208,209,7,2,0,0,209,211,3,22,11,0,210,
        207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        21,1,0,0,0,214,212,1,0,0,0,215,216,6,11,-1,0,216,217,3,24,12,0,217,
        223,1,0,0,0,218,219,10,2,0,0,219,220,7,3,0,0,220,222,3,24,12,0,221,
        218,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,
        23,1,0,0,0,225,223,1,0,0,0,226,227,6,12,-1,0,227,228,3,26,13,0,228,
        234,1,0,0,0,229,230,10,2,0,0,230,231,7,1,0,0,231,233,3,26,13,0,232,
        229,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,
        25,1,0,0,0,236,234,1,0,0,0,237,238,6,13,-1,0,238,239,3,28,14,0,239,
        245,1,0,0,0,240,241,10,2,0,0,241,242,7,4,0,0,242,244,3,28,14,0,243,
        240,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,
        27,1,0,0,0,247,245,1,0,0,0,248,249,7,5,0,0,249,252,3,28,14,0,250,
        252,3,30,15,0,251,248,1,0,0,0,251,250,1,0,0,0,252,29,1,0,0,0,253,
        254,5,2,0,0,254,255,3,16,8,0,255,256,5,3,0,0,256,264,1,0,0,0,257,
        264,5,37,0,0,258,264,5,33,0,0,259,264,5,34,0,0,260,264,5,36,0,0,
        261,264,5,31,0,0,262,264,3,46,23,0,263,253,1,0,0,0,263,257,1,0,0,
        0,263,258,1,0,0,0,263,259,1,0,0,0,263,260,1,0,0,0,263,261,1,0,0,
        0,263,262,1,0,0,0,264,31,1,0,0,0,265,266,5,23,0,0,266,267,5,2,0,
        0,267,268,3,16,8,0,268,269,5,3,0,0,269,270,5,4,0,0,270,271,3,6,3,
        0,271,272,5,5,0,0,272,33,1,0,0,0,273,274,5,24,0,0,274,275,5,2,0,
        0,275,276,3,16,8,0,276,277,5,3,0,0,277,278,5,4,0,0,278,279,3,6,3,
        0,279,281,5,5,0,0,280,282,3,36,18,0,281,280,1,0,0,0,281,282,1,0,
        0,0,282,35,1,0,0,0,283,284,5,25,0,0,284,285,5,4,0,0,285,286,3,6,
        3,0,286,287,5,5,0,0,287,37,1,0,0,0,288,289,5,32,0,0,289,290,5,6,
        0,0,290,39,1,0,0,0,291,292,5,26,0,0,292,301,5,2,0,0,293,298,3,16,
        8,0,294,295,5,7,0,0,295,297,3,16,8,0,296,294,1,0,0,0,297,300,1,0,
        0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,302,1,0,0,0,300,298,1,0,
        0,0,301,293,1,0,0,0,301,302,1,0,0,0,302,303,1,0,0,0,303,304,5,3,
        0,0,304,305,5,6,0,0,305,41,1,0,0,0,306,307,5,27,0,0,307,308,5,2,
        0,0,308,313,5,37,0,0,309,310,5,7,0,0,310,312,5,37,0,0,311,309,1,
        0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,316,1,
        0,0,0,315,313,1,0,0,0,316,317,5,3,0,0,317,318,5,6,0,0,318,43,1,0,
        0,0,319,320,5,37,0,0,320,321,5,9,0,0,321,322,3,16,8,0,322,323,5,
        6,0,0,323,45,1,0,0,0,324,325,5,37,0,0,325,334,5,2,0,0,326,331,3,
        16,8,0,327,328,5,7,0,0,328,330,3,16,8,0,329,327,1,0,0,0,330,333,
        1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,335,1,0,0,0,333,331,
        1,0,0,0,334,326,1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,336,337,
        5,3,0,0,337,47,1,0,0,0,338,340,5,28,0,0,339,341,3,16,8,0,340,339,
        1,0,0,0,340,341,1,0,0,0,341,342,1,0,0,0,342,343,5,6,0,0,343,49,1,
        0,0,0,26,53,59,74,105,113,128,132,137,149,152,172,190,201,212,223,
        234,245,251,263,281,298,301,313,331,334,340
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'const'", "'='", "'for'", "'+'", "'-'", 
                     "'||'", "'&&'", "'>'", "'<'", "'<='", "'>='", "'=='", 
                     "'!='", "'*'", "'/'", "'while'", "'if'", "'else'", 
                     "'print'", "'input'", "'return'", "<INVALID>", "'!'", 
                     "<INVALID>", "'break'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TIPO", "NOT", "BOOL", "BREAK", "INT", 
                      "REAL", "COMP", "STRING", "ID", "WS", "COMMENT_ONE_LINE", 
                      "COMMENT_MULT_LINE" ]

    RULE_prog = 0
    RULE_main = 1
    RULE_bloco = 2
    RULE_blocoFuncs = 3
    RULE_declaraVars = 4
    RULE_declaraFuncoes = 5
    RULE_funcao_for = 6
    RULE_incremento = 7
    RULE_expressao = 8
    RULE_termo = 9
    RULE_termo2 = 10
    RULE_termo3 = 11
    RULE_termo4 = 12
    RULE_termo5 = 13
    RULE_termo6 = 14
    RULE_fator = 15
    RULE_funcao_while = 16
    RULE_funcao_if = 17
    RULE_funcao_else = 18
    RULE_funcao_break = 19
    RULE_funcao_print = 20
    RULE_funcao_input = 21
    RULE_funcao_atribuicao = 22
    RULE_funcao_chamada = 23
    RULE_funcao_retorno = 24

    ruleNames =  [ "prog", "main", "bloco", "blocoFuncs", "declaraVars", 
                   "declaraFuncoes", "funcao_for", "incremento", "expressao", 
                   "termo", "termo2", "termo3", "termo4", "termo5", "termo6", 
                   "fator", "funcao_while", "funcao_if", "funcao_else", 
                   "funcao_break", "funcao_print", "funcao_input", "funcao_atribuicao", 
                   "funcao_chamada", "funcao_retorno" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    TIPO=29
    NOT=30
    BOOL=31
    BREAK=32
    INT=33
    REAL=34
    COMP=35
    STRING=36
    ID=37
    WS=38
    COMMENT_ONE_LINE=39
    COMMENT_MULT_LINE=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(gramaticaParser.MainContext,0)


        def declaraVars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DeclaraVarsContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DeclaraVarsContext,i)


        def declaraFuncoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DeclaraFuncoesContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DeclaraFuncoesContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = gramaticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.declaraVars() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==37:
                self.state = 56
                self.declaraFuncoes()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bloco(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = gramaticaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(gramaticaParser.T__0)
            self.state = 65
            self.match(gramaticaParser.T__1)
            self.state = 66
            self.match(gramaticaParser.T__2)
            self.state = 67
            self.match(gramaticaParser.T__3)
            self.state = 68
            self.bloco()
            self.state = 69
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def declaraVars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.DeclaraVarsContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.DeclaraVarsContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = gramaticaParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==29:
                self.state = 71
                self.declaraVars()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.blocoFuncs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoFuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcao_for(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_forContext,0)


        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def funcao_while(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_whileContext,0)


        def funcao_if(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_ifContext,0)


        def funcao_print(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_printContext,0)


        def funcao_input(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_inputContext,0)


        def funcao_atribuicao(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_atribuicaoContext,0)


        def funcao_chamada(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_chamadaContext,0)


        def funcao_retorno(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_retornoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_blocoFuncs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlocoFuncs" ):
                listener.enterBlocoFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlocoFuncs" ):
                listener.exitBlocoFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocoFuncs" ):
                return visitor.visitBlocoFuncs(self)
            else:
                return visitor.visitChildren(self)




    def blocoFuncs(self):

        localctx = gramaticaParser.BlocoFuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blocoFuncs)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.funcao_for()
                self.state = 80
                self.blocoFuncs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.funcao_while()
                self.state = 83
                self.blocoFuncs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.funcao_if()
                self.state = 86
                self.blocoFuncs()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.funcao_print()
                self.state = 89
                self.blocoFuncs()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.funcao_input()
                self.state = 92
                self.blocoFuncs()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.funcao_atribuicao()
                self.state = 95
                self.blocoFuncs()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.funcao_chamada()
                self.state = 98
                self.match(gramaticaParser.T__5)
                self.state = 99
                self.blocoFuncs()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 101
                self.funcao_retorno()
                self.state = 102
                self.blocoFuncs()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaraVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_declaraVars

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclaraVariaveisContext(DeclaraVarsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.DeclaraVarsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TIPO(self):
            return self.getToken(gramaticaParser.TIPO, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraVariaveis" ):
                listener.enterDeclaraVariaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraVariaveis" ):
                listener.exitDeclaraVariaveis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraVariaveis" ):
                return visitor.visitDeclaraVariaveis(self)
            else:
                return visitor.visitChildren(self)


    class DeclaraConstantesContext(DeclaraVarsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.DeclaraVarsContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def TIPO(self):
            return self.getToken(gramaticaParser.TIPO, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.STRING)
            else:
                return self.getToken(gramaticaParser.STRING, i)
        def REAL(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.REAL)
            else:
                return self.getToken(gramaticaParser.REAL, i)
        def BOOL(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.BOOL)
            else:
                return self.getToken(gramaticaParser.BOOL, i)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.INT)
            else:
                return self.getToken(gramaticaParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaraConstantes" ):
                listener.enterDeclaraConstantes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaraConstantes" ):
                listener.exitDeclaraConstantes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaraConstantes" ):
                return visitor.visitDeclaraConstantes(self)
            else:
                return visitor.visitChildren(self)



    def declaraVars(self):

        localctx = gramaticaParser.DeclaraVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaraVars)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = gramaticaParser.DeclaraVariaveisContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(gramaticaParser.TIPO)
                self.state = 108
                self.match(gramaticaParser.ID)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 109
                    self.match(gramaticaParser.T__6)
                    self.state = 110
                    self.match(gramaticaParser.ID)
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(gramaticaParser.T__5)
                pass
            elif token in [8]:
                localctx = gramaticaParser.DeclaraConstantesContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(gramaticaParser.T__7)
                self.state = 118
                self.match(gramaticaParser.TIPO)
                self.state = 119
                self.match(gramaticaParser.ID)
                self.state = 120
                self.match(gramaticaParser.T__8)
                self.state = 121
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 96636764160) != 0):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 122
                    self.match(gramaticaParser.T__6)
                    self.state = 123
                    self.match(gramaticaParser.ID)
                    self.state = 124
                    self.match(gramaticaParser.T__8)
                    self.state = 125
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 96636764160) != 0):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 130
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 131
                self.match(gramaticaParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaraFuncoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_declaraFuncoes

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Funcao_com_tipo_e_vazioContext(DeclaraFuncoesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.DeclaraFuncoesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)
        def bloco(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoContext,0)

        def TIPO(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.TIPO)
            else:
                return self.getToken(gramaticaParser.TIPO, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_com_tipo_e_vazio" ):
                listener.enterFuncao_com_tipo_e_vazio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_com_tipo_e_vazio" ):
                listener.exitFuncao_com_tipo_e_vazio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_com_tipo_e_vazio" ):
                return visitor.visitFuncao_com_tipo_e_vazio(self)
            else:
                return visitor.visitChildren(self)



    def declaraFuncoes(self):

        localctx = gramaticaParser.DeclaraFuncoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaraFuncoes)
        self._la = 0 # Token type
        try:
            localctx = gramaticaParser.Funcao_com_tipo_e_vazioContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 134
                self.match(gramaticaParser.TIPO)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(gramaticaParser.ID)
            self.state = 141
            self.match(gramaticaParser.T__1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 142
                self.match(gramaticaParser.TIPO)
                self.state = 143
                self.match(gramaticaParser.ID)
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 144
                    self.match(gramaticaParser.T__6)
                    self.state = 145
                    self.match(gramaticaParser.TIPO)
                    self.state = 146
                    self.match(gramaticaParser.ID)
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 154
            self.match(gramaticaParser.T__2)
            self.state = 155
            self.match(gramaticaParser.T__3)
            self.state = 156
            self.bloco()
            self.state = 157
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.idx = None

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def INT(self):
            return self.getToken(gramaticaParser.INT, 0)

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def incremento(self):
            return self.getTypedRuleContext(gramaticaParser.IncrementoContext,0)


        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def funcao_break(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_breakContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_for" ):
                listener.enterFuncao_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_for" ):
                listener.exitFuncao_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_for" ):
                return visitor.visitFuncao_for(self)
            else:
                return visitor.visitChildren(self)




    def funcao_for(self):

        localctx = gramaticaParser.Funcao_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcao_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(gramaticaParser.T__9)
            self.state = 160
            self.match(gramaticaParser.T__1)
            self.state = 161
            self.match(gramaticaParser.ID)
            self.state = 162
            self.match(gramaticaParser.T__8)
            self.state = 163
            self.match(gramaticaParser.INT)
            self.state = 164
            self.match(gramaticaParser.T__5)
            self.state = 165
            self.expressao(0)
            self.state = 166
            self.match(gramaticaParser.T__5)
            self.state = 167
            self.incremento()
            self.state = 168
            self.match(gramaticaParser.T__2)
            self.state = 169
            self.match(gramaticaParser.T__3)
            self.state = 170
            self.blocoFuncs()
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 171
                self.funcao_break()


            self.state = 174
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def INT(self):
            return self.getToken(gramaticaParser.INT, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_incremento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncremento" ):
                return visitor.visitIncremento(self)
            else:
                return visitor.visitChildren(self)




    def incremento(self):

        localctx = gramaticaParser.IncrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_incremento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(gramaticaParser.ID)
            self.state = 177
            self.match(gramaticaParser.T__8)
            self.state = 178
            self.match(gramaticaParser.ID)
            self.state = 179
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 180
            self.match(gramaticaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None
            self.inh_type = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_expressao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.inh_type = ctx.inh_type


    class Operacao_orContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)

        def termo(self):
            return self.getTypedRuleContext(gramaticaParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_or" ):
                listener.enterOperacao_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_or" ):
                listener.exitOperacao_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_or" ):
                return visitor.visitOperacao_or(self)
            else:
                return visitor.visitChildren(self)


    class Vai_termoContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(gramaticaParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo" ):
                listener.enterVai_termo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo" ):
                listener.exitVai_termo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo" ):
                return visitor.visitVai_termo(self)
            else:
                return visitor.visitChildren(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 183
            self.termo(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_orContext(self, gramaticaParser.ExpressaoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    self.match(gramaticaParser.T__12)
                    self.state = 187
                    self.termo(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Operacao_andContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(gramaticaParser.TermoContext,0)

        def termo2(self):
            return self.getTypedRuleContext(gramaticaParser.Termo2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_and" ):
                listener.enterOperacao_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_and" ):
                listener.exitOperacao_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_and" ):
                return visitor.visitOperacao_and(self)
            else:
                return visitor.visitChildren(self)


    class Vai_termo2Context(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo2(self):
            return self.getTypedRuleContext(gramaticaParser.Termo2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo2" ):
                listener.enterVai_termo2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo2" ):
                listener.exitVai_termo2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo2" ):
                return visitor.visitVai_termo2(self)
            else:
                return visitor.visitChildren(self)



    def termo(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.TermoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_termo, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termo2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 194
            self.termo2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_andContext(self, gramaticaParser.TermoContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo)
                    self.state = 196
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 197
                    self.match(gramaticaParser.T__13)
                    self.state = 198
                    self.termo2(0) 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Operacao_comparacaoContext(Termo2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo2Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo2(self):
            return self.getTypedRuleContext(gramaticaParser.Termo2Context,0)

        def termo3(self):
            return self.getTypedRuleContext(gramaticaParser.Termo3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_comparacao" ):
                listener.enterOperacao_comparacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_comparacao" ):
                listener.exitOperacao_comparacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_comparacao" ):
                return visitor.visitOperacao_comparacao(self)
            else:
                return visitor.visitChildren(self)


    class Vai_termo3Context(Termo2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo3(self):
            return self.getTypedRuleContext(gramaticaParser.Termo3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo3" ):
                listener.enterVai_termo3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo3" ):
                listener.exitVai_termo3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo3" ):
                return visitor.visitVai_termo3(self)
            else:
                return visitor.visitChildren(self)



    def termo2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Termo2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_termo2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termo3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 205
            self.termo3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_comparacaoContext(self, gramaticaParser.Termo2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo2)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self.termo3(0) 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Vai_termo4Context(Termo3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo4(self):
            return self.getTypedRuleContext(gramaticaParser.Termo4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo4" ):
                listener.enterVai_termo4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo4" ):
                listener.exitVai_termo4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo4" ):
                return visitor.visitVai_termo4(self)
            else:
                return visitor.visitChildren(self)


    class Operacao_igual_difContext(Termo3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo3Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo3(self):
            return self.getTypedRuleContext(gramaticaParser.Termo3Context,0)

        def termo4(self):
            return self.getTypedRuleContext(gramaticaParser.Termo4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_igual_dif" ):
                listener.enterOperacao_igual_dif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_igual_dif" ):
                listener.exitOperacao_igual_dif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_igual_dif" ):
                return visitor.visitOperacao_igual_dif(self)
            else:
                return visitor.visitChildren(self)



    def termo3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Termo3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_termo3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termo4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 216
            self.termo4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_igual_difContext(self, gramaticaParser.Termo3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo3)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 220
                    self.termo4(0) 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Vai_termo5Context(Termo4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo5(self):
            return self.getTypedRuleContext(gramaticaParser.Termo5Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo5" ):
                listener.enterVai_termo5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo5" ):
                listener.exitVai_termo5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo5" ):
                return visitor.visitVai_termo5(self)
            else:
                return visitor.visitChildren(self)


    class Operacao_soma_subContext(Termo4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo4Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo4(self):
            return self.getTypedRuleContext(gramaticaParser.Termo4Context,0)

        def termo5(self):
            return self.getTypedRuleContext(gramaticaParser.Termo5Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_soma_sub" ):
                listener.enterOperacao_soma_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_soma_sub" ):
                listener.exitOperacao_soma_sub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_soma_sub" ):
                return visitor.visitOperacao_soma_sub(self)
            else:
                return visitor.visitChildren(self)



    def termo4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Termo4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_termo4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termo5Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 227
            self.termo5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_soma_subContext(self, gramaticaParser.Termo4Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo4)
                    self.state = 229
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 230
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==11 or _la==12):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.termo5(0) 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Operacao_multi_divContext(Termo5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo5Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo5(self):
            return self.getTypedRuleContext(gramaticaParser.Termo5Context,0)

        def termo6(self):
            return self.getTypedRuleContext(gramaticaParser.Termo6Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_multi_div" ):
                listener.enterOperacao_multi_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_multi_div" ):
                listener.exitOperacao_multi_div(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_multi_div" ):
                return visitor.visitOperacao_multi_div(self)
            else:
                return visitor.visitChildren(self)


    class Vai_termo6Context(Termo5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo6(self):
            return self.getTypedRuleContext(gramaticaParser.Termo6Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_termo6" ):
                listener.enterVai_termo6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_termo6" ):
                listener.exitVai_termo6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_termo6" ):
                return visitor.visitVai_termo6(self)
            else:
                return visitor.visitChildren(self)



    def termo5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Termo5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_termo5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Vai_termo6Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 238
            self.termo6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 245
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.Operacao_multi_divContext(self, gramaticaParser.Termo5Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_termo5)
                    self.state = 240
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 241
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 242
                    self.termo6() 
                self.state = 247
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Termo6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_termo6

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class Operacao_menos_notContext(Termo6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo6Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def termo6(self):
            return self.getTypedRuleContext(gramaticaParser.Termo6Context,0)

        def NOT(self):
            return self.getToken(gramaticaParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacao_menos_not" ):
                listener.enterOperacao_menos_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacao_menos_not" ):
                listener.exitOperacao_menos_not(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacao_menos_not" ):
                return visitor.visitOperacao_menos_not(self)
            else:
                return visitor.visitChildren(self)


    class Vai_fatorContext(Termo6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Termo6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def fator(self):
            return self.getTypedRuleContext(gramaticaParser.FatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVai_fator" ):
                listener.enterVai_fator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVai_fator" ):
                listener.exitVai_fator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVai_fator" ):
                return visitor.visitVai_fator(self)
            else:
                return visitor.visitChildren(self)



    def termo6(self):

        localctx = gramaticaParser.Termo6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_termo6)
        self._la = 0 # Token type
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 30]:
                localctx = gramaticaParser.Operacao_menos_notContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==12 or _la==30):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.termo6()
                pass
            elif token in [2, 31, 33, 34, 36, 37]:
                localctx = gramaticaParser.Vai_fatorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.fator()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return gramaticaParser.RULE_fator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class Terminal_intContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(gramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_int" ):
                listener.enterTerminal_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_int" ):
                listener.exitTerminal_int(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_int" ):
                return visitor.visitTerminal_int(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_stringContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_string" ):
                listener.enterTerminal_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_string" ):
                listener.exitTerminal_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_string" ):
                return visitor.visitTerminal_string(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_booleanContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(gramaticaParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_boolean" ):
                listener.enterTerminal_boolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_boolean" ):
                listener.exitTerminal_boolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_boolean" ):
                return visitor.visitTerminal_boolean(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_funcao_chamadaContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcao_chamada(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_chamadaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_funcao_chamada" ):
                listener.enterTerminal_funcao_chamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_funcao_chamada" ):
                listener.exitTerminal_funcao_chamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_funcao_chamada" ):
                return visitor.visitTerminal_funcao_chamada(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_floatContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(gramaticaParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_float" ):
                listener.enterTerminal_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_float" ):
                listener.exitTerminal_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_float" ):
                return visitor.visitTerminal_float(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_abre_fecha_expressaoContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_abre_fecha_expressao" ):
                listener.enterTerminal_abre_fecha_expressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_abre_fecha_expressao" ):
                listener.exitTerminal_abre_fecha_expressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_abre_fecha_expressao" ):
                return visitor.visitTerminal_abre_fecha_expressao(self)
            else:
                return visitor.visitChildren(self)


    class Terminal_idContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal_id" ):
                listener.enterTerminal_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal_id" ):
                listener.exitTerminal_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_id" ):
                return visitor.visitTerminal_id(self)
            else:
                return visitor.visitChildren(self)



    def fator(self):

        localctx = gramaticaParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fator)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.Terminal_abre_fecha_expressaoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(gramaticaParser.T__1)
                self.state = 254
                self.expressao(0)
                self.state = 255
                self.match(gramaticaParser.T__2)
                pass

            elif la_ == 2:
                localctx = gramaticaParser.Terminal_idContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 3:
                localctx = gramaticaParser.Terminal_intContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(gramaticaParser.INT)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.Terminal_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(gramaticaParser.REAL)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.Terminal_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.match(gramaticaParser.STRING)
                pass

            elif la_ == 6:
                localctx = gramaticaParser.Terminal_booleanContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.match(gramaticaParser.BOOL)
                pass

            elif la_ == 7:
                localctx = gramaticaParser.Terminal_funcao_chamadaContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.funcao_chamada()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_while" ):
                listener.enterFuncao_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_while" ):
                listener.exitFuncao_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_while" ):
                return visitor.visitFuncao_while(self)
            else:
                return visitor.visitChildren(self)




    def funcao_while(self):

        localctx = gramaticaParser.Funcao_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcao_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(gramaticaParser.T__22)
            self.state = 266
            self.match(gramaticaParser.T__1)
            self.state = 267
            self.expressao(0)
            self.state = 268
            self.match(gramaticaParser.T__2)
            self.state = 269
            self.match(gramaticaParser.T__3)
            self.state = 270
            self.blocoFuncs()
            self.state = 271
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def funcao_else(self):
            return self.getTypedRuleContext(gramaticaParser.Funcao_elseContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_if" ):
                listener.enterFuncao_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_if" ):
                listener.exitFuncao_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_if" ):
                return visitor.visitFuncao_if(self)
            else:
                return visitor.visitChildren(self)




    def funcao_if(self):

        localctx = gramaticaParser.Funcao_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcao_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(gramaticaParser.T__23)
            self.state = 274
            self.match(gramaticaParser.T__1)
            self.state = 275
            self.expressao(0)
            self.state = 276
            self.match(gramaticaParser.T__2)
            self.state = 277
            self.match(gramaticaParser.T__3)
            self.state = 278
            self.blocoFuncs()
            self.state = 279
            self.match(gramaticaParser.T__4)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 280
                self.funcao_else()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocoFuncs(self):
            return self.getTypedRuleContext(gramaticaParser.BlocoFuncsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_else" ):
                listener.enterFuncao_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_else" ):
                listener.exitFuncao_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_else" ):
                return visitor.visitFuncao_else(self)
            else:
                return visitor.visitChildren(self)




    def funcao_else(self):

        localctx = gramaticaParser.Funcao_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcao_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(gramaticaParser.T__24)
            self.state = 284
            self.match(gramaticaParser.T__3)
            self.state = 285
            self.blocoFuncs()
            self.state = 286
            self.match(gramaticaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(gramaticaParser.BREAK, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_break" ):
                listener.enterFuncao_break(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_break" ):
                listener.exitFuncao_break(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_break" ):
                return visitor.visitFuncao_break(self)
            else:
                return visitor.visitChildren(self)




    def funcao_break(self):

        localctx = gramaticaParser.Funcao_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcao_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(gramaticaParser.BREAK)
            self.state = 289
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_print

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assignment_printContext(Funcao_printContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Funcao_printContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_print" ):
                listener.enterAssignment_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_print" ):
                listener.exitAssignment_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_print" ):
                return visitor.visitAssignment_print(self)
            else:
                return visitor.visitChildren(self)



    def funcao_print(self):

        localctx = gramaticaParser.Funcao_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcao_print)
        self._la = 0 # Token type
        try:
            localctx = gramaticaParser.Assignment_printContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(gramaticaParser.T__25)
            self.state = 292
            self.match(gramaticaParser.T__1)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 235149463556) != 0:
                self.state = 293
                self.expressao(0)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 294
                    self.match(gramaticaParser.T__6)
                    self.state = 295
                    self.expressao(0)
                    self.state = 300
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 303
            self.match(gramaticaParser.T__2)
            self.state = 304
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_input

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assignment_inputContext(Funcao_inputContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Funcao_inputContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_input" ):
                listener.enterAssignment_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_input" ):
                listener.exitAssignment_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_input" ):
                return visitor.visitAssignment_input(self)
            else:
                return visitor.visitChildren(self)



    def funcao_input(self):

        localctx = gramaticaParser.Funcao_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcao_input)
        self._la = 0 # Token type
        try:
            localctx = gramaticaParser.Assignment_inputContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(gramaticaParser.T__26)
            self.state = 307
            self.match(gramaticaParser.T__1)
            self.state = 308
            self.match(gramaticaParser.ID)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 309
                self.match(gramaticaParser.T__6)
                self.state = 310
                self.match(gramaticaParser.ID)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316
            self.match(gramaticaParser.T__2)
            self.state = 317
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_atribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_atribuicao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Expressao_atribContext(Funcao_atribuicaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Funcao_atribuicaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_atrib" ):
                listener.enterExpressao_atrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_atrib" ):
                listener.exitExpressao_atrib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao_atrib" ):
                return visitor.visitExpressao_atrib(self)
            else:
                return visitor.visitChildren(self)



    def funcao_atribuicao(self):

        localctx = gramaticaParser.Funcao_atribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcao_atribuicao)
        try:
            localctx = gramaticaParser.Expressao_atribContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(gramaticaParser.ID)
            self.state = 320
            self.match(gramaticaParser.T__8)
            self.state = 321
            self.expressao(0)
            self.state = 322
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_chamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_chamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_chamada" ):
                listener.enterFuncao_chamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_chamada" ):
                listener.exitFuncao_chamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_chamada" ):
                return visitor.visitFuncao_chamada(self)
            else:
                return visitor.visitChildren(self)




    def funcao_chamada(self):

        localctx = gramaticaParser.Funcao_chamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcao_chamada)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(gramaticaParser.ID)
            self.state = 325
            self.match(gramaticaParser.T__1)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 235149463556) != 0:
                self.state = 326
                self.expressao(0)
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 327
                    self.match(gramaticaParser.T__6)
                    self.state = 328
                    self.expressao(0)
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 336
            self.match(gramaticaParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funcao_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcao_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao_retorno" ):
                listener.enterFuncao_retorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao_retorno" ):
                listener.exitFuncao_retorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao_retorno" ):
                return visitor.visitFuncao_retorno(self)
            else:
                return visitor.visitChildren(self)




    def funcao_retorno(self):

        localctx = gramaticaParser.Funcao_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcao_retorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(gramaticaParser.T__27)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 235149463556) != 0:
                self.state = 339
                self.expressao(0)


            self.state = 342
            self.match(gramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expressao_sempred
        self._predicates[9] = self.termo_sempred
        self._predicates[10] = self.termo2_sempred
        self._predicates[11] = self.termo3_sempred
        self._predicates[12] = self.termo4_sempred
        self._predicates[13] = self.termo5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def termo_sempred(self, localctx:TermoContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def termo2_sempred(self, localctx:Termo2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def termo3_sempred(self, localctx:Termo3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def termo4_sempred(self, localctx:Termo4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def termo5_sempred(self, localctx:Termo5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




