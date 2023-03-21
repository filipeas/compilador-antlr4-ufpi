grammar gramatica;

prog: declaraVars* declaraFuncoes* main;

main:
    'main' '(' ')' '{' bloco '}';

// forcar declaraVars para usar somente no inicio do bloco
bloco: declaraVars* blocoFuncs;

blocoFuncs:
      funcao_for blocoFuncs
    | funcao_while blocoFuncs
//    | funcao_break blocoFuncs
    | funcao_if blocoFuncs
    | funcao_print blocoFuncs
    | funcao_input blocoFuncs
    | funcao_atribuicao blocoFuncs
    | funcao_chamada ';' blocoFuncs
    | funcao_retorno blocoFuncs
//    | declaraVars blocoFuncs
    |
    ;

declaraVars:
      TIPO ID (',' ID)* ';' #declaraVariaveis
    | 'const' TIPO ID '=' op=(STRING | REAL | BOOL | INT) (',' ID '=' op=(STRING | REAL | BOOL | INT))* ';' #declaraConstantes
    ;

declaraFuncoes:
      TIPO* ID '(' (TIPO ID (',' TIPO ID)*)? ')' '{' bloco '}' #funcao_com_tipo_e_vazio;

funcao_for returns [idx]
    : 'for' '(' ID '=' op=(INT | ID) ';' expressao ';' incremento ')' '{' blocoFuncs funcao_break? '}';
incremento:
      ID '=' ID op=('+' | '-') INT
    ;

expressao returns [type, inh_type]
    : expressao '||' termo  #operacao_or
    | termo                 #vai_termo
    ;

termo returns [type]:
      termo '&&' termo2     #operacao_and
    | termo2                #vai_termo2
    ;

termo2 returns [type]:
      termo2 op=('>' | '<' | '<=' | '>=') termo3    #operacao_comparacao
    | termo3                                        #vai_termo3
    ;

termo3 returns [type]:
      termo3 op=('==' | '!=') termo4    #operacao_igual_dif
    | termo4                            #vai_termo4
    ;

termo4 returns [type]:
      termo4 op=('+' | '-') termo5      #operacao_soma_sub
    | termo5                            #vai_termo5
    ;

termo5 returns [type]:
      termo5 op=('*' | '/') termo6      #operacao_multi_div
    | termo6                             #vai_termo6
    ;

termo6 returns [type]:
       op=('-' | NOT) termo6 #operacao_menos_not
     | fator #vai_fator
     ;

fator returns [type]:
      '(' expressao ')'     #terminal_abre_fecha_expressao
    | ID                    #terminal_id
    | INT                   #terminal_int
    | REAL                 #terminal_float
    | STRING                #terminal_string
    | BOOL               #terminal_boolean
    | funcao_chamada #terminal_funcao_chamada
    ;

funcao_while: 'while' '(' expressao ')' '{' blocoFuncs '}';
funcao_if: 'if' '(' expressao ')' '{' blocoFuncs '}' funcao_else?;
funcao_else: 'else' '{' blocoFuncs '}';
funcao_break: BREAK ';';
funcao_print: 'print' '(' (expressao (',' expressao)*)? ')' ';' #assignment_print;
funcao_input: 'input' '(' ID (',' ID)* ')' ';' #assignment_input;
funcao_atribuicao: ID '=' expressao ';' #expressao_atrib;
funcao_chamada: ID '(' (expressao (',' expressao)*)? ')';
funcao_retorno: 'return' (expressao)? ';';

// **********
// DEFINIÇÕES
// **********
// fazer comentario de uma linha e multiplas linhas
TIPO: 'int' | 'real' | 'bool' | 'String';
fragment DIGIT: [0-9];
NOT: '!';
BOOL: 'true' | 'false';
BREAK: 'break';
INT: DIGIT+;
REAL: DIGIT+ '.' DIGIT+ ;
COMP: '==' | '!=' | '>=' | '<=' | '>' | '<';
STRING: '"' .*? '"';
ID: [a-zA-Z1-9]+;
WS : [ \t\r\n]+ -> skip ;
COMMENT_ONE_LINE: '//' .*? '\n' -> skip;
COMMENT_MULT_LINE: '/*' .*? '*/' -> skip;
