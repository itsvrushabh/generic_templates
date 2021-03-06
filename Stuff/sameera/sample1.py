from textfsm import TextFSM
import sys


def f1(input_file, template_file):
    try:
        _tm = TextFSM(open(template_file))
        _raw = open(input_file).read()
        _header = _tm.header
        _fsm = _tm.ParseText(_raw)
        print("-".center(100, "-"))
        print(_raw)
        print("-".center(100, "-"))
        print(_header)
        print("-".center(100, "-"))
        print(_fsm)
        print("-".center(100, "-"))
        for j in [dict(zip(_header, i)) for i in _fsm]:
            print(j)
        print("-".center(100, "-"))
        print(len(_fsm))
        print("-".center(100, "-"))
    except Exception as e:
        raise e


if __name__ == "__main__":
    input_file = sys.argv[1]----------------------------------------------------------------------------------------------------
['SOURCE', 'TIME', 'SEVERITY', 'SYSLOG_STRING', 'DESCRIPTION']
----------------------------------------------------------------------------------------------------
[['GigabitEthernet0/0/1', 'Sep 06 2019 00:11:00', 'INFO', 'ETHERNET_PORT_ADMIN_DOWN', 'Physical Port Administrative State Down [2]'], ['GigabitEthernet0/0/2', 'Oct 11 2019 18:41:07', 'INFO', 'ETHERNET_PORT_ADMIN_DOWN', 'Physical Port Administrative State Down [2]'], ['xcvr container 0/0/3', 'Oct 01 2019 13:35:29', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/0/4', 'Sep 06 2019 00:10:32', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/0/5', 'Sep 06 2019 00:10:32', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/0/6', 'Sep 06 2019 00:10:32', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/0/7', 'Sep 06 2019 00:10:32', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['TenGigabitEthernet0/0/8', 'Sep 06 2019 00:11:00', 'INFO', 'ETHERNET_PORT_ADMIN_DOWN', 'Physical Port Administrative State Down [2]'], ['xcvr container 0/1/1', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/2', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/3', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/4', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/5', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/6', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['xcvr container 0/1/7', 'Sep 06 2019 00:10:31', 'INFO', 'XCVR_MISSING', 'Transceiver Missing [0]'], ['TenGigabitEthernet0/1/8', 'Oct 01 2019 15:21:03', 'INFO', 'ETHERNET_PORT_ADMIN_DOWN', 'Physical Port Administrative State Down [2]']]
----------------------------------------------------------------------------------------------------
{'SOURCE': 'GigabitEthernet0/0/1', 'TIME': 'Sep 06 2019 00:11:00', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'ETHERNET_PORT_ADMIN_DOWN', 'DESCRIPTION': 'Physical Port Administrative State Down [2]'}
{'SOURCE': 'GigabitEthernet0/0/2', 'TIME': 'Oct 11 2019 18:41:07', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'ETHERNET_PORT_ADMIN_DOWN', 'DESCRIPTION': 'Physical Port Administrative State Down [2]'}
{'SOURCE': 'xcvr container 0/0/3', 'TIME': 'Oct 01 2019 13:35:29', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING', 'DESCRIPTION': 'Transceiver Missing [0]'}
{'SOURCE': 'xcvr container 0/0/4', 'TIME': 'Sep 06 2019 00:10:32', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING', 'DESCRIPTION': 'Transceiver Missing [0]'}
{'SOURCE': 'xcvr container 0/0/5', 'TIME': 'Sep 06 2019 00:10:32', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING', 'DESCRIPTION': 'Transceiver Missing [0]'}
{'SOURCE': 'xcvr container 0/0/6', 'TIME': 'Sep 06 2019 00:10:32', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING',er Missing [0]'}
{'SOURCE': 'xcvr container 0/1/6', 'TIME': 'Sep 06 2019 00:10:31', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING', 'DESCRIPTION': 'Transceiver Missing [0]'}
{'SOURCE': 'xcvr container 0/1/7', 'TIME': 'Sep 06 2019 00:10:31', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'XCVR_MISSING', 'DESCRIPTION': 'Transceiver Missing [0]'}
{'SOURCE': 'TenGigabitEthernet0/1/8', 'TIME': 'Oct 01 2019 15:21:03', 'SEVERITY': 'INFO', 'SYSLOG_STRING': 'ETHERNET_PORT_ADMIN_DOWN', 'DESCRIPTIO
C:\Users\SAMEERA\Documents\GitHub\generic_templates\sameera>
























































































































    template_file = sys.argv[2]
    f1(input_file, template_file)
