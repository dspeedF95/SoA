import os
import sys
import re
import io
# assert len(sys.argv) == 3, "usage:\ntxtsplit.py <input_file_name> <output_dir>"
# iname = str(sys.argv[1])
# odir = str(sys.argv[2])

ifile = io.open(r'chinese.txt', 'r', encoding='utf-16')

string_stripped_list = []

for i, line in enumerate(ifile.readlines()):
    pattern = r'\\(?!.*?\\)(.*?)(?:\~|\.)|(?:\$.*>>\:|\$.*>>\: )(.*?)<(?:/|a|s|d|img|font)|<p>(?!<<)(.*?)<(?:/|a|s|d|img|font)|">(?!<<)(.*?)<(?:/|a|s|d|img|font)|(?:if \$ |if\$|if \$|if \$|\$ |\$)(.*?(?<!ARGS\[0\]))(?:>|\[|<|\=|\!|\+|\-|\*|/| )|data\-title\=".*?"|\'\'(.*?)\'\'|gs\'(.*?)\'|# (.*?)|if \$ARGS\[0\]\="(.*?)"\:'
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
string_stripped_list.index("缝合之地的魔王担心不下你，故与你交换了一只魔瞳，保护你的同时时刻监视着你。受到魔王之力的加持，你的全属性上升了5点。")
#%%
import xml.etree.ElementTree as ET
from xml.dom import minidom
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, encoding='utf-8', method='xml')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# assert len(sys.argv) == 3, "usage:\nqprojgen.py <input_dir> <output_file_name>"
# idir = str(sys.argv[1])
# oname = str(sys.argv[2])
ofile = io.open('chinese_xml_dict.xml', 'w', encoding='utf-8', newline='\r\n')
root = ET.Element("dictionary")
location_holder = ET.SubElement(root, 'Structure')
for string in string_stripped_list:
    ET.SubElement(root, "entry", attrib={"original": string, "translated": ""})
xml_file = prettify(root)
ofile.write(xml_file)
ofile.close()