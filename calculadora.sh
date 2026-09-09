#!/bin/bash
# Script Shell para automatizar a execução da calculadora Python

echo "Inicializando a calculadora..."
sleep 1

# Executa o script Python que você criou
python3 calculadora.py


echo "=== CALCULADORA SH ==="
echo "Digite o primeiro número:"
read num1
echo "Digite o segundo número:"
read num2

echo "Escolha a operação:"
echo "1 - Soma (+)"
echo "2 - Subtração (-)"
echo "3 - Multiplicação (*)"
echo "4 - Divisão (/)"
read opcao

case $opcao in
    1)
        resultado=$((num1 + num2))
        echo "Resultado da Soma: $resultado"
        ;;
    2)
        resultado=$((num1 - num2))
        echo "Resultado da Subtração: $resultado"
        ;;
    3)
        resultado=$((num1 * num2))
        echo "Resultado da Multiplicação: $resultado"
        ;;
    4)
        if [ $num2 -eq 0 ]; then
            echo "Erro: Divisão por zero não é permitida!"
        else
            resultado=$((num1 / num2))
            echo "Resultado da Divisão: $resultado"
        fi
        ;;
    *)
        echo "Opção inválida!"
        ;;
esac
