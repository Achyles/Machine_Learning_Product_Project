# -*- coding: utf-8 -*-
"""

@author: Achyles
"""

"""
A word embedding model takes a wordList and a scoreList
and embeds each word with its frequency and the average score it receives.

The model is saved in a dictionary.

Prediction returns the score of the word.
"""

class WordEmbed():
    
    def __init__(self):
        self.embed = dict();
    
    def train(self, wordList, scoreList):
        for i in range(len(wordList)):
            for w in wordList[i]:
                if w not in self.embed:
                    self.embed.update({w:[scoreList[i],1]})
                else:
                    post = self.embed[w]
                    newscore = (post[0]*post[1]+scoreList[i])/(post[1]+1)
                    self.embed.update({w:[newscore,post[1]+1]})
        
       
    def predict(self,key):
        return self.embed[key][0]

    
    def getModel(self):
        return self.embed
