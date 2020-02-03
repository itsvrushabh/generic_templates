from __future__ import absolute_import
import sys
import datetime
from textfsm import TextFSM
import netmiko

class TextFSMHandler:
    def __init__(self):
        self._fsm = []
        self._template = ""

    def get_command_fsm(self, command_output, template_name):
        """ sample docstring """
        _res = {}
        try:
            self._template = TextFSM(open(template_name)) 
            _raw = open(command_output).read()    
            self._fsm = self._template.ParseText(_raw)
            _res['PARSE_OUTPUT'] = bool(len(self._fsm))
            _res['fsm'] = self._fsm
            _res['fsm_dict'] = [dict(zip(self._template.header, fsm))
                                for fsm in self._fsm]
            _res['header'] = self._template.header
        except Exception as _e:
            _res['output'] = str(_e)
            _res['PARSE_OUTPUT'] = False
            _res['fsm_dict'] = []
            _res['header'] = []
        print (_res)
        print("-".center(100, "-"))
        data = []
        for j in [dict(zip(self._template.header, i)) for i in self._fsm]:
            print(j)
            data.append(j)
        print("-".center(100, "-"))



x = TextFSMHandler()
command_output = sys.argv[1]
template_name = sys.argv[2]
x.get_command_fsm(command_output, template_name)