#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import fonctions
import data

def game():
	fonctions.player_name()
	fonctions.word_validation(fonctions.generation_word())
	end_game=False
	while end_game==False:
		fonctions.tour()
		end_game=fonctions.end_game()
	print(fonctions.after_end_game())
	if fonctions.check_word_find()==True:
		fonctions.save_score(data.player_name,data.lives)

game()