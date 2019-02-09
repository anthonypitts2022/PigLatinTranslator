# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:00:56 2019

@author: AnthonyPitts
"""

word = input("Type the word you want to translate or type '.' to quit: ")
vowels = 'aeiou'
while(word!='.'): #user wants to play again
    def piggify( word ):
        if(word[0] in vowels): #starts with a vowel
            translatedWord = word + 'yay'
        if(word[0] not in vowels): #starts with a consonant
            firstConsonants = '' #holds the consonants before first vowel
            firstVowel = -1 #location of first vowel
            for i in range(0,(len(word)-1)):
                if(word[i] not in vowels):
                    firstConsonants= firstConsonants + word[i]
                else:
                    firstVowel = i
                    break
            if(firstVowel == -1): # no vowels
                translatedWord = word + 'ay'
            else:
                word = word[firstVowel: len(word)]
                translatedWord = word + firstConsonants + 'ay'
        print(translatedWord)
        return translatedWord
    piggify(word)
    
    word = input("Type the word you want to translate or type '.' to quit: ")

    
