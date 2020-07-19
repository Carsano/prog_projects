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

def ask_letter():
	can_play = False
	while not can_play:
		letter = input("Please choose a letter: ")
		can_play, message = can_play_letter(letter)
		print(message)
	save_letter(letter)

def can_play_letter(letter):
	if not letter.isalpha():
		message = "This is not a playable character"
		return False, message
	elif letter in data.false_letters or letter in data.found_letters:
		message = "You've already played this letter"
		return False, message
	else:
		message = "Let's go"
		return True, message

def print_false_letters():
	print(data.false_letters)

def print_found_letters():
	print(data.found_letters)

def send_letter_good_false(letter_booelan):
	if letter_booelan[1]:
		data.found_letters.append(letter_booelan[0])
	else:
		data.false_letters.append(letter_booelan[0])

def save_letter(letter):
	send_letter_good_false(letter_check(letter))

# Validated

#def nom_joueur():
	# demande le nom du joueur 
	# enregistre ce nom dans donnes

#def enregistrer_score():
	# ouvre ou crée fichier scores
	# enregistre son nom avec le score 0

def lose_life():
	data.lives -= 1
	return data.lives


#def tour():
	# joue un tour de pendu
	# affiche le mot caché
	# demande au joueur de taper une lettre
	# vérifie la lettre
	# affiche si le joueur a trouvé une lettre ou pas
	# enlève une vie si besoin


word_validation(generation_word())
ask_letter()
print_false_letters()