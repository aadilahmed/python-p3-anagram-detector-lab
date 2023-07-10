class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagram = sorted([letter for letter in self.word])
        return_list = []
        for word in word_list:
            temp_list = sorted([letter for letter in word])
            if anagram == temp_list:
                return_list.append(word)
        
        return return_list
