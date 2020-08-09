#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import fonctions

def game():
	fonctions.generation_words()
	end_game=False
	while end_game==False:
		fonctions.tour()
		end_game=fonctions.end_game
	print(fonctions.after_end_game)