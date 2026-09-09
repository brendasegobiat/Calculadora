#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def executar_calculadora():
    print("--- CALCULADORA EM PYTHON ---")
    try:
        # Pede as entradas de dados ao usuário através do terminal
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
        sys.exit(1)

    print("\nEscolha uma opção:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    opcao = input("Digite a opção desejada: ")

    # Estrutura lógica traduzida do script Shell original
    if opcao == "1":
        resultado = num1 + num2
        print(f"\nResultado da Soma: {resultado}")
    elif opcao == "2":
        resultado = num1 - num2
        print(f"\nResultado da Subtração: {resultado}")
    elif opcao == "3":
        resultado = num1 * num2
        print(f"\nResultado da Multiplicação: {resultado}")
    elif opcao == "4":
        if num2 == 0:
            print("\nErro: Divisão por zero não é permitida!")
            sys.exit(1)
        else:
            resultado = num1 / num2
            print(f"\nResultado da Divisão: {resultado}")
    else:
        print("\nOpção inválida!")
        sys.exit(1)

if __name__ == "__main__":
    executar_calculadora()
