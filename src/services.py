
from __future__ import absolute_import
import sys
import datetime
from textfsm import TextFSM
import netmiko


class TextFSMHandler:
    """
    Textfsm handler class 
    """
    def insert_to_csv(self, _record):
        self.csv_file.write(_record+"\n")

    def __init__(self):
        """
        Init value to default
        """
        self._fsm = []
        self._template = None
        self._json_output = []
        self._status = False
        self._header = []
        self.csv_file = open('output_template.csv', 'w')

    def get_command_fsm(self, command_output, template_name):
        """ sample docstring"""
        try:
            self._template = TextFSM(open(template_name))
            self._fsm = self._template.ParseText(command_output)
            self._json_output = [dict(zip(self._template.header, fsm))
                                 for fsm in self._fsm]
            self._header = self._template.header
            self._status = True
            self.name = template_name
        except Exception:
            raise

    def get_template_accuracy(self):
        no_of_records = len(self._json_output)
        no_of_header_attribute = len(self._header)
        percetange_of_record = 100 / no_of_records
        percetange_of_attribute = percetange_of_record/no_of_header_attribute
        template_percetange = 0
        temp_name = self.name


        for i in self._json_output:
            for j in self._header:
                if i[j] != '':
                    template_percetange += percetange_of_attribute
        print("-".center(100, "-"))
        print("Template_Location:",temp_name)
        print("Accuracy :",template_percetange,"%")
        print("No_of_Header:" ,no_of_header_attribute)
        print("No_of_Records:" ,no_of_records)
        print("Percentage_of_Record" ,percetange_of_record)
        print("Percentage_of_attribute" ,percetange_of_attribute)
        print("-".center(100, "-"))

        csv_output_record = temp_name+","+str(template_percetange)+","+str(no_of_header_attribute)+","+str(no_of_records)+","+str(percetange_of_record)+","+str(percetange_of_attribute)
        self.insert_to_csv(csv_output_record)
       

    