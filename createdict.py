import os
import sys
import re
import io
import dicttoxml
from xml.dom.minidom import parseString
# assert len(sys.argv) == 3, "usage:\ntxtsplit.py <input_file_name> <output_dir>"
# iname = str(sys.argv[1])
# odir = str(sys.argv[2])

ifile = io.open(r'chinese.txt', 'r', encoding='utf-16')

string_stripped_list = []

for i, line in enumerate(ifile.readlines()):
    pattern = r'<p>(.*?(?<!</a>))<(?:/p>|a|s)|">(.*?(?<!</a>))<(?:/p|a|s|d)|(?:if |if|\$ |\$)(.*?(?<!ARGS\[0\]))(?:>|\[|<|\=|\!| )|data\-title\=".*?"|\'\'(.*?)\'\'|gs\'(.*?)\'|# (.*?)|if \$ARGS\[0\]\="(.*?)":'
    matches = re.findall(pattern, line)
    for i, tuple_of in enumerate(matches):
        matches[i] = list(tuple_of)
    flat_list = []
    for sublist in matches:
        for item in sublist:
            flat_list.append(item)
            
    if matches:
        string_stripped_list.extend(flat_list)
string_stripped_list = [string for string in string_stripped_list if string]
res = []
[res.append(x) for x in string_stripped_list if x not in res]
#%%
string_stripped_list.index("日期计数君")