
# Linguagem: FrogLang
# Grupo: Os FrogLang
# Integrantes: Felipe Amaro Souza de Jesus || RA : 924110739

from lexer_parser3 import parser

comandos = [
    # PRINTS e INPUTS
    'System.out.println("Hello World");',
    'System.out.println("Testando o println");',
    'JOptionPane.ShowInputDialog("Digite algo");',

    # VARIÁVEIS
    'int contador = 10;',
    'float media = a + b + 3;',
    'x = y + 5;',
    'z = 2 + 2 + w;',

    # LOOPS
    'for("loop for iniciado");',
    'while("condição de loop");',
    'do',

    # CONDICIONAIS
    'if("a > b")',
    'else',

    # FUNÇÕES MAIN
    'public static void main(args)',
    'def main(args)',

    # IMPORTAÇÃO / INCLUSÃO DE BIBLIOTECAS
    'import javax.swing;',
    'import math;',
    '#include<stdio.h>',

    # MAIS VARIÁVEIS
    'int numero = 5;',
    'float resultado = numero + 4;'
    'a = b + 10;',

    # COMANDOS MISTOS
    'if("x == y")',
    'System.out.println("Comparando x e y");',
    'else',
    'System.out.println("Diferentes");',

    'while("i < 10")',
    'System.out.println("Dentro do while");',

    'do',
    'System.out.println("Executa pelo menos uma vez");',
    'for("int i = 0; i < 5; i++")'
]

for linha in comandos:
    print("\nLinha:", linha)
    parser.parse(linha)
