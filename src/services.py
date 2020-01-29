"""


"""
from __future__ import absolute_import
import sys
import datetime
from textfsm import TextFSM
from netmiko import Netmiko
class TextFSMHandler:
    def __init__(self):
        self._fsm = []
        self._template = ""

    def get_command_fsm(self, command_output, template_name):
        """ sample docstring"""
        _res = {}
        try:
            self._template = TextFSM(open(TEMPLATE_LOCATION+template_name))
            self._fsm = _template.ParseText(command_output)
            _res['PARSE_OUTPUT'] = bool(len(self._fsm))
            _res['fsm'] = self._fsm
            _res['fsm_dict'] = [dict(zip(_template.header, fsm))
                                for fsm in self._fsm]
            _res['header'] = self._template.header
        except Exception as _e:
            _res['output'] = str(_e)
            _res['PARSE_OUTPUT'] = False
            _res['fsm_dict'] = []
            _res['header'] = []
        return _res
