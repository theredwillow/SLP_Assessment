import nltk

class GV(object):
    def tokenizeme(self, LanguageSample):
        self.tokenized_text=nltk.word_tokenize(LanguageSample)
        self.unique_words=list(set(self.tokenized_text))
        self.unique_words.sort()
        self.unique_words=nltk.pos_tag(self.unique_words) #Unique words does not get rid of infectional morpheme duplicates
        self.tagged_text = [i for i in nltk.pos_tag(self.tokenized_text) if i[1]!="."] #pos_tag gets the part of speech, loop removes punctuation
        self.count = len(self.tagged_text)
            #Right now, unique_words removes duplicates of noun vs verb
            #You need to find a way to remove duplicates from multidimensional list
