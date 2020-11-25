from tkinter import *
from classes import Dog

class GUI:
    def __init__(self, parent):
        """
        Setup string var, label to display and two btns
        one to change text, the other to quit
        """
        # Create a string var
        self.__label_text = StringVar()
        self.__label_text.set("Hello, World!")
    
        self.__counter = IntVar()
        self.__counter.set(0)

        # Create and display a label
        Label(parent, textvariable=self.__label_text).pack()
        Label(parent, textvariable=self.__counter).pack()

        # Create and display a button to change the text
        self.__button_change = Button(parent,
                                      text="Change Text",
                                      command=self.change_text)
        self.__button_change.pack()

        # Create and display quit button
        Button(parent, text="Quit", command=quit).pack()

    def change_text(self):
        """ Change the label """
        self.__label_text.set("Goodbye Cruel World!")
        #kimchi = Dog("tan","poofy",1)
        #self.__label_text.set(kimchi.get_colour())

    def adder(self):
        self.__counter.set(self.__counter.get()+1)

if __name__ == "__main__":
    root = Tk()
    GUI(root)
    root.mainloop() # Halt execution
