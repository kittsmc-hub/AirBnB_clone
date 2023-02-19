#!/usr/bin/python3
import cmd

"""
This module contains a command interpreter for HBNB.
"""


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        """ greet [person]
        Greet the named person"""
        print("hello")

    prompt = (("hbnb:"))

    def do_EOF(self, line):
        """ EOF command to exit the program"""
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
