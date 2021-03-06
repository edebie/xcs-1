"""
Name:        xcs_config_parser.py
Authors:     Bao Trung
Contact:     baotrung@ecs.vuw.ac.nz
Created:     July, 2017
Description:
---------------------------------------------------------------------------------------------------------------------------------------------------------
XCS: Michigan-style Learning Classifier System - A LCS for Reinforcement Learning.  This XCS follows the version descibed in "An Algorithmic Description of XCS" published by Martin Butz and Stewart Wilson (2002).

---------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#Import Required Modules----------
from xcs_constants import *
#import os
#---------------------------------

class ConfigParser:
    def __init__(self, filename):
        self.comment_char = '#'
        self.param_char = '='
        self.parameters = self.parseConfig(filename) #Parse the configuration file and get all parameters.
        cons.setConstants(self.parameters) #Store run parameters in the 'Constants' module.


    def parseConfig(self, filename):
        """ Parses the configuration file. """
        parameters = {}
        try:
            f = open(filename)
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
            print('cannot open', filename)
            raise
        else:
            for line in f:
                #Remove text after comment character.
                if self.comment_char in line:
                    line, comment = line.split(self.comment_char, 1) #Split on comment character, keep only the text before the character

                #Find lines with parameters (param=something)
                if self.param_char in line:
                    parameter, value = line.split(self.param_char, 1) #Split on parameter character
                    parameter = parameter.strip() #Strip spaces
                    value = value.strip()
                    parameters[parameter] = value #Store parameters in a dictionary

            f.close()

        return parameters

