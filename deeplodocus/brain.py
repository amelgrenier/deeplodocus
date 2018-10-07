import os.path
import time

from deeplodocus.utils.notification import Notification, DEEP_ERROR, DEEP_INPUT, DEEP_SUCCESS, DEEP_FATAL, DEEP_WARNING
from deeplodocus.utils.namespace import Namespace
from deeplodocus.utils.logo import Logo
from deeplodocus.utils.end import End
from deeplodocus.utils.logs import Logs
from deeplodocus.ui.user_interface import UserInterface


class Brain(object):

    def __init__(self, config_path):
        self.config_path = config_path
        self.logs = ["notification"]
        self.__init_logs()
        self.version = "0.1.0"
        Logo(version=self.version)
        self.exit_flags = ["q", "quit", "exit"]
        self.config = None
        self.user_interface = None
        self.__load_config()

    def wake(self):
        """
        Authors : Alix Leroy
        Main of deeplodocus framework
        :return: None
        """
        while True:
            command = Notification(DEEP_INPUT, "Waiting for instruction...").get()
            command = command.replace(" ", "")
            if command in self.exit_flags:
                break
            else:
                self.__run_command(command)
                time.sleep(0.2)                 # Sleep to make sure that asynchronous commands are completed
        if self.user_interface is not None:
            self.user_interface.stop()
        End(error=False)

    def __run_command(self, command):
        """
        :param command:
        :return:
        """
        # Load a new config file
        if command == "load_config":
            self.__load_config()
        # train the network
        elif command == "train":
            print("Train")
        # Start the User Interface
        elif command == "ui" or command == "user_interface" or command == "interface":
            if self.user_interface is None:
                self.user_interface = UserInterface()
            else:
                Notification(DEEP_ERROR, "The user interface is already running")
        elif command == "ui_stop" or command == "stop_ui" or command == "ui stop":
            if self.user_interface is not None:
                self.user_interface.stop()
                self.user_interface = None
        else:
            Notification(DEEP_WARNING, "The given command does not exist.")

    def __init_logs(self):
        """
        Authors : Alix Leroy
        Initialize all logs
        :return:None
        """
        for log_name in self.logs:
            Logs(log_name).check_init()
        Notification(DEEP_SUCCESS, "Logs initialized ! ")

    def __load_config(self):
        """
        Author: SW
        Function: Checks current config path is valid, if not, user is prompted to give another
        :return: bool: True if a valid config path is set, otherwise, False
        """
        while True:
            if os.path.isfile(self.config_path):
                self.config = Namespace(self.config_path)
                Notification(DEEP_SUCCESS, "Config file loaded (%s)" % self.config_path)
                return True
            else:
                Notification(DEEP_ERROR, "Given path does not point to a file (%s)" % self.config_path)
                self.config_path = Notification(DEEP_INPUT, "Please insert the config file path :").get()
                if self.config_path in self.exit_flags:
                    return False


if __name__ == "__main__":
    import argparse


    def main(args):
        config = args.c

        brain = Brain(config)
        brain.wake()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", type=str, default="config/config_depthnet.yaml",
                        help="Path to the config yaml file")
    arguments = parser.parse_args()
    main(arguments)
