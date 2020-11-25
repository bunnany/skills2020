from tkinter import *

class GUI:
    def __init__(self, parent):
        """
        Setup string var, label to display and two btns
        one to change text, the other to quit
        """
        # Create a string var
        self.__label_text = StringVar()
        self.__label_text.set("Hello, World!")

        # Create and display a label
        Label(parent, textvariable=self.__label_text).pack()

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

if __name__ == "__main__":
    root = Tk()
    GUI(root)
    root.mainloop() # Halt
