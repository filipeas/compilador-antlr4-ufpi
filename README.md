# Compilador Simplificado

Projeto de compilador simplificado, imitando sintaxe do Python.

Essa versão foi feita para passar na disciplina de compiladores - UFPI, logo mais talvez eu coloque a versão real que estava fazendo (com Golang, escrevendo tudo do zero, sem bibliotecas!).

## Passos iniciais
- Primeiro baixe o java jdk no seu pc.
- Depois baixe o python 3 (pode usar anaconda)
- Depois instale o antlr4 no python [clique aqui](antlr.org)

## Como executar:
- Verifique se você possui o jasmin.jar (está nesse repositório). Ele é necessário para gerar o .class
- Execute: ``` java -jar jasmin.jar nome_do_programa.j ```
- Execute: ``` java nome_do_programa ```

## Funcionalidades:
- escrever variavel local
- escrever variavel global
- escrever constante local
- escrever constante global
- verificar break opcional no bloco do for (na parte semantica)
- for
- while
- if
- else
- break
- print
- input
- funcao chamada