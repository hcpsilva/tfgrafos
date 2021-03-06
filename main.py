import os
import sys
from grafo import Grafo

"""Implementacao do algoritmo de Dijkstra em Python.

Trabalho final da disciplina de Grafos e Analise Combinatoria
UFRGS - Instituto de Informatica
2017/2

Henrique Correa Pereira da Silva    -   262508
Maria Clara Machry Jacintho         -   262505
"""


entrada = Grafo(os.path.abspath(sys.argv[1]))
try:
    if sys.argv[4] == '-passo':
        print(entrada)
        passo = True
    else:
        passo = False
except IndexError:
    passo = False
entrada.dijkstra(int(sys.argv[2]), int(sys.argv[3]), passo)
