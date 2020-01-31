import sys
from difflib import SequenceMatcher


def f1(text_file, json_file):
    text1 = open(text_file).read()
    text2 = open(json_file).read()
    m = SequenceMatcher(None, text1, text2)
    val = m.ratio()
    print (val )


if __name__ == "__main__":
    text_file = sys.argv[1]
    json_file = sys.argv[2]
    f1(text_file, json_file)