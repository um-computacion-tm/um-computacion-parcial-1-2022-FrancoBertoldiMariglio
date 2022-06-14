import re
from unittest import mock
from invalidassignmentexception import InvalidAssignmentException

class Hangman():
    def __init__(self):
        self.lifes = 5
        self.word = str
        self.wordMade = ''
        self.wordTemporary = []
        self.wordRepetida = []
    
    def set_word(self, word):
        if type(word) != str:
            raise InvalidAssignmentException
        palabra = word.lower()
        self.word = palabra
        for i in range(len(self.word)):
            self.wordMade = self.wordMade + '_ '
            self.wordTemporary.append('_')
            
    def show(self):
        return ('Lifes: ' + str(self.lifes) + ' - Word: ' + self.wordMade)

    def assign(self, letter):
            letra = letter.lower()
            if type(letra) != str:
                raise InvalidAssignmentException
            if letra not in self.word:
                self.lifes -= 1
                raise InvalidAssignmentException
            if letra not in self.wordRepetida:
                self.wordRepetida.append(letra)
            else:
                raise InvalidAssignmentException
           
            contador = 0
            indice = []
            self.wordMade = ''

            for i in self.word:
                if i == letra:
                    indice.append(contador)
                    contador += 1
                else:
                    contador += 1
                    continue
            
            for i in indice:
                self.wordTemporary[i] = (self.word[i])
            
            for i in range(len(self.word)):
                self.wordMade = self.wordMade + self.wordTemporary[i] + ' '

    def winner(self):
        variable = self.word
        for i in range(len(self.word)):
                variable = self.word[i] + ' '
        if self.wordMade.lower() == variable.lower():
                return True
        else:
                return False
    def play(self):
        
        self.assign(mock)
        if self.winner == True:
            return 'Ganaste'
        else:
            return 'Perdiste'
         
            
