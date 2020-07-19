#!/usr/bin/python3.8

# -*-coding:UTF-8 -*
import data


import random


def generation_word():
	word = random.choice(data.word_dictionnary)
	return word

def word_validation(word):
	data.word_to_find = word


def letter_check(letter):
	if letter in data.word_to_find:
		return letter, True
	else:
		return letter, False

# Validated
def ask_letter():
	# demande à l'utilisateur de rentrer une lettre
	# check si la lettre peut être rentrée
	# return la lettre
	letter = input("Please choose a letter: ")
	can_paly = False
	while can_play == False:
		can_play = can_play_letter(letter)
	return letter

def can_play_letter(letter):
	# vérifie que la lettre est bien une lettre
	# vérifie que la lettre n'a pas déjà été jouée
	# return true ou false
	if not letter.isalpha():
		print("This is not a playable character")
		return False
	elif letter in false_letters or letter in found_letters:
		print("You've already played this letter")
		return False
	else:
		return True

def print_false_letters():
	# affiche la liste des lettres_fausses
	print(false_letters)

def send_letter_good_false(letter, boolean):
	# envoie la lettre dans la liste bonne ou dans la liste fausse
	if boolean:
		found_letters.append(letter)
	else:
		found_letters.append(letter)


#def nom_joueur():
	# demande le nom du joueur 
	# enregistre ce nom dans donnes

#def enregistrer_score():
	# ouvre ou crée fichier scores
	# enregistre son nom avec le score 0

def lose_life(lives):
	lives -= 1
	return lives


#def tour():
	# joue un tour de pendu
	# affiche le mot caché
	# demande au joueur de taper une lettre
	# vérifie la lettre
	# affiche si le joueur a trouvé une lettre ou pas
	# enlève une vie si besoin


word_validation(generation_word())
