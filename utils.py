import base64
from fontTools.ttLib import TTFont
import re
from xml.dom.minidom import parse

def get_base64_str(origin_str):

    base64_str = re.findall('"data:application/octet-stream;base64,([\s\S]*?)"', origin_str)[0]

    return base64_str


def get_map_dict(base64_str):

    decoded = base64.b64decode(base64_str)
    with open('font.woff', 'wb') as f:
        f.write(decoded)
    font = TTFont('font.woff')
    font.saveXML('font_replace.xml')

    xml_doc = parse('font_replace.xml')
    root = xml_doc.documentElement
    cmap = root.getElementsByTagName('cmap_format_4')[0]
    map_list = cmap.getElementsByTagName('map')
    map_dict ={}
    for m in map_list:
        if m.getAttribute('code') != "0x78":
            code_str = '&#'+m.getAttribute('code')[1:]
            name = m.getAttribute('name')[3:]
            name_str = chr(int(name, 16))
            map_dict[code_str] = name_str

    return map_dict


def exchange_str(map_dict, origin_str):
    for k in map_dict.keys():
        origin_str = origin_str.replace(k, map_dict[k])

    return origin_str