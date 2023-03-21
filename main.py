import os
from antlr4 import *
from gen.gramaticaLexer import gramaticaLexer
from gen.gramaticaParser import gramaticaParser
from myGramaticaListener import gramaticaListener

if __name__ == '__main__':
    file = FileStream("exemplo_if_print_e_input.txt")

    # parte lexica
    lexer = gramaticaLexer(file)
    streams = CommonTokenStream(lexer)

    # parte analise sintatica
    parser = gramaticaParser(streams)
    tree = parser.prog()

    # parte analise semantica
    filename = 'programa_final'
    l = gramaticaListener(filename)
    walker = ParseTreeWalker()
    walker.walk(l, tree)

    # executar o programa .j
    # os.system('java -jar jasmin.jar {}'.format(filename + '.j'))
    # os.system('java {}'.format(filename))