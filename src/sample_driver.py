from services import TextFSMHandler
from utils import csv_record


def factory_func(template, command_output_file_loc, template_file_loc):
    command_output = open(command_output_file_loc).read()
    template.get_command_fsm(command_output, template_file_loc)
    if template._status:
        template.get_template_accuracy()
    else:
        raise Exception('Template have some issue')


if __name__ == "__main__":
     template = TextFSMHandler()
    # print(csv_record)
     for i in csv_record:
    #     print(i[0],i[1])
        factory_func(template, i[0], i[1])
    # factory_func(template, '../Stuff/Vishak/Cisco_xe/cisco_xe_show_access-list/show_acces-list.txt', '../Stuff/Vishak/Cisco_xe/cisco_xe_show_access-list/show_acces-list.textfsm')
