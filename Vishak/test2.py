import textfsm
import sys

# Open the template file, and initialise a new TextFSM object with it.
template_file = sys.argv[1]
fsm = textfsm.TextFSM(open(template_file))

# Read stdin until EOF, then pass this to the FSM for parsing.
input_data = sys.stdin.read()
fsm_results = fsm.ParseText(input_data)

print ('Header:')
print (fsm.header)

print ('Prefix             | Gateway(s)')
print ('-------------------------------')

for row in fsm_results:
  print ('%-18.18s  %s' % (row[2], ', '.join(row[3])))