import nltk

LanguageSample = open("LanguageSample.txt", 'r').read()
print "Here is the sample provided:"
print LanguageSample

tokenized_text=nltk.word_tokenize(LanguageSample)
print tokenized_text

tagged_text=nltk.pos_tag(tokenized_text)
print tagged_text

print ""
print "A terminable unit (or \"T-unit\") consists of one main clause and all the subordinate clauses attached to it (Hunt, 1965). It is primarily used to segment written samples." 
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentences=sent_detector.tokenize(LanguageSample.strip())
print sentences

print ""
print "A communication unit (or \"C-unit\", or \"CU\") consists of each independent clause with its modifiers (Loban, 1976). It is primarily used to segment oral samples."
for sentence in sentences:
    tokenized_sentence=nltk.word_tokenize(sentence)
    tagged_sentence=nltk.pos_tag(tokenized_sentence)
    verbs=[x for x in nltk.pos_tag(tokenized_sentence) if x[0] in ["VB","VBD","VBG","VBN","VBP","VBZ"]]
    print verbs
    """
    if sum([word_pos[1] for word_pos in nltk.pos_tag(tokenized_sentence)].count(x) for x in 'VB VBD VBG VBN VBP VBZ'.split()) > 1:
        window=Tkinter.Tk()
        w = Tkinter.Label(window, text="What is the client's name?")
        window.w.pack()
        name = Tkinter.StringVar()
        namebox = Tkinter.Entry(window,textvariable=name)
        window.namebox.pack()
        submitbutton = Tkinter.Button(window, text = "Submit", command=self.submitInfo)
        window.submitbutton.pack()
        window.mainloop()
        sentence+="          (This sentence is suspicious.)"
    print sentence
    """

"""
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
"""
