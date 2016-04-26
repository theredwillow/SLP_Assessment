import Tkinter
import tkMessageBox
import tkFileDialog
import sys
import NLTK_Info

class NewWindow(object):
    def __init__(self, scene):
        self.master=Tkinter.Tk()
        self.scene=scene
        self.master.wm_title("Type-Token Ratio")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        if scene is "ClientInfo":
            self.showClientInfo()
        elif scene is "LanguageSample":
            self.showLanguageSample()
        elif scene is "Information":
            self.showInformation()
        elif scene is "CompoundWords":
            self.showCompoundWords()
        self.master.mainloop()

    def showInformation(self):
        self.info="""The type-token ratio (TTR) is an easy-to-calculate measure of functional vocabulary skills. The ratio reflects the diversity of words used by the client during the language sample.\n
                    Templin (1957) reported that normally developing children between the ages of 3 and 8 years have TTRs of .45-.50. A substandard TTR is one indicator of an expressive language delay or disorder.\n
                    TTR is calculated by transcribing a language sample, then counting the total words and the number of different words produced by the client.\n
                    To calculate the TTR, divide the number of different words by the total number of words in the sample."""
        self.w = Tkinter.Label(self.master, text=self.info)
        self.w.pack()
        self.nextbutton = Tkinter.Button(self.master, text = "Next", command=self.master.destroy)
        self.nextbutton.pack()

    def showClientInfo(self):
        self.w = Tkinter.Label(self.master, text="What is the client's name?")
        self.w.pack()
        self.name = Tkinter.StringVar()
        self.namebox = Tkinter.Entry(self.master,textvariable=self.name)
        self.namebox.pack()
        self.x = Tkinter.Label(self.master, text="What is the client's age?")
        self.x.pack()
        self.age = Tkinter.StringVar()
        self.agebox = Tkinter.Entry(self.master,textvariable=self.age)
        self.agebox.pack()
        self.gender = Tkinter.StringVar()
        self.boy = Tkinter.Radiobutton(self.master, text="Boy", variable=self.gender, value="boy")
        self.boy.pack()
        self.girl = Tkinter.Radiobutton(self.master, text="Girl", variable=self.gender, value="girl")
        self.girl.pack()
        self.submitbutton = Tkinter.Button(self.master, text = "Submit", command=self.submitInfo)
        self.submitbutton.pack()
    
    def showLanguageSample(self):
        self.w = Tkinter.Label(self.master, text="The first thing we need is your language sample. You can type it into the text field or upload a text file.")
        self.w.pack()
        self.textbox = Tkinter.Text(self.master)
        self.textbox.pack()
        self.uploadbutton = Tkinter.Button(self.master, text = "Upload .txt file", command=self.getFile)
        self.uploadbutton.pack()        
        self.submitbutton = Tkinter.Button(self.master, text = "Submit", command=self.submitInfo)
        self.submitbutton.pack()

    def showCompoundWords(self):
        self.pressedbuttons=[]
        self.wordbuttons={}
        self.rowcount=1
        self.columncount=1
        print "Here's the tagged text: BOOOOOOOOOOOOOOOOOOOOYYYYYYYYYYYYYYYYYYY"
        print tagged_text
        for index, word in enumerate(tagged_text):
            self.wordbuttons[index] = Tkinter.Button(self.master, text = word[0], command = lambda i=index:self.wordPressed(i))
            self.wordbuttons[index].grid(row=rowcount,column=columncount,sticky="W")
            self.columncount+=1
            if self.columncount > wordsperline:
                self.rowcount+=1
                self.columncount=1

    def wordPressed(buttonpressed):
        if self.buttonpressed not in self.pressedbuttons:
            self.wordbuttons[self.buttonpressed].configure(relief = "sunken")
            self.pressedbuttons.append(self.buttonpressed)
        else:
            self.wordbuttons[self.buttonpressed].configure(relief = "raised")
            self.pressedbuttons.remove(self.buttonpressed)
    
    def getFile(self):
        filename = tkFileDialog.askopenfilename()
        if filename:
            self.sample = open(filename, 'r').read()
            self.master.destroy()

    def submitInfo(self):
        if self.scene is "ClientInfo":
            self.genderandname=[self.name.get(),self.gender.get(),self.age.get()]
        elif self.scene is "LanguageSample":
            self.sample=self.textbox.get("1.0",'end-1c')
        self.master.destroy()

    def on_closing(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()
            sys.exit()
