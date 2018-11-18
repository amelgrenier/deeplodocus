from deeplodocus.utils.logs import Logs
from deeplodocus.utils.flags.log import *


class End(object):
    """
    Authors : Alix Leroy,
    Terminates the program
    """

    def __init__(self, error):
        """
        Authors : Alix Leroy
        Terminates the program
        :param error: Whether the program terminated with an error or not
        """
        if error is False :
            self.__thanks_master()
        # Stop the program
        raise SystemExit(0)

    def __thanks_master(self):
        """
        Authors: Alix Leroy
        Display thanks message
        :return: Universal Love <3
        """

        print("\n=================================")
        print("Thank you for using Deeplodocus !")
        print("== Made by Humans with deep <3 ==")
        print("=================================\n")
