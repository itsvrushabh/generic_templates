import sys
from textfsm import TextFSM

def func(txt_file,tmpl_file):
    try:
        tm = TextFSM(open(tmpl_file))
        raw = open(txt_file).read()
        header = tm.header
        fsm = tm.ParseText(raw)
        print(raw)
        print(header)
        print(fsm)

    except Exception as e:
        raise e


if __name__ == "__main__":
    txt_file = sys.argv[1]
    tmpl_file = sys.argv[2]
    func(txt_file, tmpl_file)