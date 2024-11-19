class palin :
    def __init__(self,word):
        self.word=word
    def check(self):
        self.r=self.word[::-1]
        if self.r==self.word:
          print('it is a palindrome')
        else:
          print('it is not a palindrome')
words=palin(input('enter your word'))
words.check()