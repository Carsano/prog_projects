#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import fonctions

def game():
	fonctions.word_validation(fonctions.generation_word())
	end_game=False
	while end_game==False:
		fonctions.tour()
		end_game=fonctions.end_game()
	print(fonctions.after_end_game)

game()