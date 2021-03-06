##
# dog.py
# construct a dog class
# @author NY


class Dog:
    """
    Dogs have hair colour and type
    As defined here they can only bark
    and give their age in human years
    """

    def __init__(self, __colour, __hair, __age):
        """
        Construct a new Dog object
        @param colour - a string for the colour of the dog's hair
        @param hair - a string for the type of hair the dog has
        @param years - an int giving the dogs age in years
        """
        # Define our instance variables
        self.__colour = __colour
        self.__hair = __hair
        self.__age = __age

    def bark(self):
        """
        outputs "Woof!"
        """
        print("Woof!")

    def human_age(self):
        """
        @return an int of the age of the dog in human years
        """
        return self.__age*7


if __name__ == "__main__":
    fido = Dog("brown", "wiry", 3)
    rex = Dog("grey", "short", 4)
    kimchi = Dog("tan", "poofy", 1)
