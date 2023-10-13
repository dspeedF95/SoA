import os
import sys
import re
import io
import dicttoxml
from xml.dom.minidom import parseString
# assert len(sys.argv) == 3, "usage:\ntxtsplit.py <input_file_name> <output_dir>"
# iname = str(sys.argv[1])
# odir = str(sys.argv[2])

ifile = io.open(r'main/bank.qsrc', 'r', encoding='utf-8')

string_dict = {}
string_stripped_dict = {}

for i, line in enumerate(ifile.readlines()):
    pattern = r'">\w.*<|p>\w.*<'
    pattern_2 = r'data-title=".*?"'
    matches = re.search(pattern, line)
    if matches:
        text_stripped = matches.group(0)
        text_stripped = text_stripped[2:]
        text_stripped = text_stripped[:-1]
        if text_stripped[0:2] == '<a':
            matches = re.search(pattern_2, line)
            if matches is not None:
                text_stripped = matches.group(0)
            else:
                matches = re.search(pattern, text_stripped)
                text_stripped = matches.group(0)
                text_stripped = text_stripped[1:]
                text_stripped = text_stripped[:-1]
        if text_stripped[0:4] == '<img':
            text_stripped = ""
            string_dict[i] = line
        elif len(text_stripped) >= 0:
            if "</a>" in text_stripped:
                text_stripped = text_stripped.replace("</a>", "")
            text_pointer = line.find(text_stripped)
            string_stripped_dict[i] = [text_pointer]
            string_stripped_dict[i].append(text_stripped)
            string_dict[i] = line.replace(text_stripped, '')
    elif (re.search(pattern_2, line)) is not None:
        matches = re.search(pattern_2, line)
        text_stripped = matches.group(0)
        if len(text_stripped) >= 0:
            text_pointer = line.find(text_stripped)
            string_stripped_dict[i] = [text_pointer]
            string_stripped_dict[i].append(text_stripped)
            string_dict[i] = line.replace(text_stripped, '')
    else:
        string_dict[i] = line

xml = dicttoxml.dicttoxml(string_dict)
dom = parseString(xml)
pretty_xml_as_string = dom.toprettyxml()
ofile = io.open('bank.xml', 'w', encoding='utf-8')
ofile.write(pretty_xml_as_string)

xml = dicttoxml.dicttoxml(string_stripped_dict)
dom = parseString(xml)
pretty_xml_as_string = dom.toprettyxml()
ofile = io.open('bank_stripped.xml', 'w', encoding='utf-8')
ofile.write(pretty_xml_as_string)