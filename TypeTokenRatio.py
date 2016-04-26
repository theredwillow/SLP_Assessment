import re
import collections
import TTR_GUI

[Client,Gender,Age] = TTR_GUI.NewWindow("ClientInfo").genderandname
LanguageSample = TTR_GUI.NewWindow("LanguageSample").sample
wordsperline=20
TTR_GUI.NewWindow("Information")

print "Here's the sample"
print LanguageSample

"""
UPenn Part of Speech Reference
Number Tag    Description
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
"""

def specialized_pos(sample,pos):
    if pos is "nouns":
        return [i for i,x in sample if x == "NN" or x == "NNS" or x == "NNP" or x =="NNPS"]
    if pos is "verbs":
        return [i for i,x in sample if x == "VB" or x == "VBD" or x == "VBG" or x =="VBN" or x=="VBP" or x=="VBZ" or x == "MD"]
    if pos is "adjectives":
        return [i for i,x in sample if x == "JJ" or x == "JJR" or x == "JJS"]
    if pos is "adverbs":
        return [i for i,x in sample if x == "RB" or x == "RBR" or x == "RBS"]
    if pos is "prepositions":
        return [i for i,x in sample if x == "IN"]
    if pos is "pronouns":
        return [i for i,x in sample if x == "PRP" or x == "PRP$"]
    if pos is "conjunctions":
        return [i for i,x in sample if x == "CC"]
    if pos is "affneg":
        return [i for i,x in sample if i == "yes" or i == "no" or i == "sure" or i == "yeah"]
    if pos is "articles":
        return [i for i,x in sample if x == "DT"]
    if pos is "whwords":
        return [i for i,x in sample if x == "WDT" or x == "WP" or x == "WP$" or x == "WRB"]

import NLTK_Info
globalvariables=NLTK_Info.GV().tokenizeme(LanguageSample)
tokenized_text=globalvariables.tokenized_text
unique_words=globalvariables.unique_words
tagged_text = globalvariables.tagged_text
count = globalvariables.count


print "Here is the language sample after it has been tagged for parts of speech:"
print tagged_text

print ""
print "These are "+str(len(unique_words))+" unique words in this language sample. They are:"
print unique_words

print ""
print "By using the Natural Language Processing Toolkit, we find that the total word count is "+str(count)+" words."
print "However, this does not account for compound words with spaces, such as \"ice cream\" or \"post office\". Can you see any in the language sample?"

#This tk GUI window is pretty ugly, need to work on aesthetics
pressedbuttons=TTR_GUI.NewWindow("CompoundWords").pressedbuttons

#Iteration does not account for more-than-three-word compound words
compoundwords=[]
for number,value in enumerate(pressedbuttons):
    if number < len(pressedbuttons)-1:
        if pressedbuttons[number+1] == value+1:
            compoundwords.append(value)

#Left off at: altering the tagged_text, removing compound words
        
print "Excellent, I'll recalculate the totals after I FIX THIS STUPID SCRIPT!!!"
print ""

#This is the P-O-S counter
tag_fd = nltk.FreqDist(tag for (word, tag) in tagged_text)
pos_count = tag_fd.most_common()

tag_uniques = nltk.FreqDist(tag for (word, tag) in unique_words)
pos_count_uniques = tag_uniques.most_common()

#can't get word counter to sort while ignoring case and keeping counts
print "Would you like the word counter in numbers or x's?"
numorx=raw_input()
print "Here is a word counter for this language sample:"
for pos in ["nouns","verbs","adjectives","adverbs","prepositions","pronouns","conjunctions","affneg","articles","whwords"]:
    pos_text=specialized_pos(tagged_text,pos)
    counter=collections.Counter(pos_text)
    counter=sorted(counter.items())
    print pos.title()+":"
    if numorx == "numbers":
        print counter
    else:
         for word,occurances in counter:
             xs=""
             if occurances > 1:
                 for i in range(occurances-1):
                     xs+=" X"
             print word+" "+xs
    print "Total: "+str(len(counter))+" unique words and "+str(len(pos_text))+" tokens"
    print "Percentage: "+str(int(100*(float(len(counter))/float(len(unique_words)))))+"% of all unique words and "+str(int(100*(float(len(pos_text))/float(len(tagged_text)))))+"% of all tokens"
    print ""

print "Here is a part of speech counter for all of the words in this language sample:"
print pos_count
print ""
print "And here is a part of speech counter for all of the unique words in this language sample:"
print pos_count_uniques

print ""
print "SUMMARY:"
ttr=float(len(unique_words))/float(count)
print "The client, "+Client+", has a type-token ratio (TTR) of "+str(ttr)+"."
print "This was calculated by dividing the total number of unique words, "+str(len(unique_words))+", by the total number of all words, "+str(count)+"."
if ttr >= 0.6:
    print "This is an unusually high TTR, most clients score below 50%. It's possible that the sample is not large enough to be truly representative."
elif ttr >= 0.5 and ttr < 0.6:
    print "This is an impressive TTR, most clients score below 50%."
elif ttr >= 0.45 and ttr < 0.5:
    print "This is a average TTR because it is between 0.45 and 0.5."
elif ttr >= 0.3 and ttr < 0.45:
    print "This is a slightly below average TTR. Most clients score at least 0.45."
elif ttr >= 0.25 and ttr < 0.3:
    print "This is a low TTR. This student could probably benefit from speech-language pathology therapy."
else:
    print "This is an unusually low TTR. It's possible that the sample is not truly representative of the client's potential."
print Client+" has a well-established vocabulary of " #this is going to be a synopsis of the parts of speech
print "From this language sample, it looks like she isn't using many " #again, parts of speech synopsis

raw_input()
