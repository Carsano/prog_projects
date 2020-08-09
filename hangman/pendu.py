#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import fonctions
import data

def game():
	fonctions.introduction()
	fonctions.player_name()
	scores = fonctions.score_begin_game()
	fonctions.word_validation(fonctions.generation_word())
	end_game=False
	while end_game==False:
		fonctions.tour()
		end_game=fonctions.end_game()
	print(fonctions.after_end_game())
	if fonctions.check_word_find()==True:
		scores[data.player_name] += data.lives
		fonctions.save_score(scores)

game()