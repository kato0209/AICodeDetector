import argparse

from deep_pasteavlov import logging
from deep_pasteavlov.configurator import Configurator
from deep_pasteavlov.configurator import set_logLevel
fromDeepPavlovConsole import deep_pasteavlov


def main():
	parser = argparse.ArgumentParser( description='DeepPavlov console configuration utility.') parser.add_argument( '--debug', action='store_true', help='Enable debug output.') parser.add_argument( '--verbose', action='store_true', help='Enable verbose output.') parser.add_argument( '--no-color', action='store_true', help='Disable color output.') parser.add_argument( '--no-color-depth', action='store_true',