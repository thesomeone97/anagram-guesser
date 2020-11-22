# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:09:33 2020

@author: thiag
"""


def exercicio_118(nome_arq = 'lista_de_palavras.txt'):
	"""Sorteia uma palavra de uma lista de palavras, a qual será embaralhada
	(anagrama), e o usuário deverá tentar adivinhar qual é a palavra em 6
	tentativas."""
	#sorteando uma palavra do arquivo de texto.
	import random
	with open(nome_arq) as f:
		num_linhas = sum(1 for linha in f)
	linha_escolhida = random.randint(1,num_linhas)
	arq = open(nome_arq)
	linha = 1
	while linha < linha_escolhida:
		arq.readline()
		linha += 1
	palavra = arq.readline().upper().replace('\n','')
	arq.close()
	def embaralha_palavra(word):
		"""Recebe uma string word, e retorna uma string embaralhada com os
		mesmos caracteres."""
		lista_palavra = list(word)
		lista_palavra_trocada = lista_palavra.copy()
		tamanho = len(word)
		#A seguir, produzimos uma lista contendo as posições originais
		#das letras de word (começando a contar do 0).
		posicoes = list(range(tamanho))
		#Hora de permutar as posições aleatoriamente.
		for i in range(tamanho):
			j = random.randint(i,tamanho-1)
			posicoes[i],posicoes[j] = posicoes[j],posicoes[i]
		for i in range(tamanho):
			lista_palavra_trocada[i] = lista_palavra[posicoes[i]]
		return "".join(lista_palavra_trocada)
	#iniciando modo REPL
	primeira_vez = True
	numero_de_erros = 0
	palavra_embaralhada = embaralha_palavra(palavra)
	acertou = False
	while True:
		if primeira_vez:
			print("PALAVRA EMBARALHADA\n--------------------------------\n")
			primeira_vez = False
		print(palavra_embaralhada)
		chute = input("Qual é a palavra? ").upper()
		if not chute.isalpha():
			print("Chute inválido! Tente novamente.")
			continue
		if chute == palavra:
			acertou = True
		else:
			numero_de_erros += 1
			print(f"Você errou pela {numero_de_erros}ª vez! Tente novamente.\n")
		if acertou:
			print(f"\nParabéns! Você venceu. A palavra era: {palavra}")
			break
		if numero_de_erros == 6:
			print(f"Você perdeu! A palavra era: {palavra}")
			break
		
if __name__ == '__main__':
	exercicio_118()
