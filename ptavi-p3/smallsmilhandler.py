#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    def __init__(self):

        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.all = []


    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == "root-layout":
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get("width", "")
            self.height = attrs.get("height", "")
            self.background_color = attrs.get("background-color", "")
            self.all.append({ "name": name, "width": self.width, "height": self.height,
            "background_color": self.background_color })

        elif name == "region":
            self.id = attrs.get("id", "")
            self.top = attrs.get("top", "")
            self.bottom = attrs.get("bottom", "")
            self.left = attrs.get("left", "")
            self.right = attrs.get("right", "")
            self.all.append({ "name": name, "id": self.id, "top": self.top, "bottom": self.bottom,
            "left": self.left, "right": self.right})

        elif name == "img":
            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.all.append({ "name": name, "src": self.src, "region": self.region,
            "begin": self.begin, "dur": self.dur})
        elif name == "audio":

            self.src = attrs.get("src", "")
            self.begin = attrs.get("begin", "")
            self.dur = attrs.get("dur", "")
            self.all.append({"name": name, "src": self.src, "begin": self.begin,
            "dur": self.dur})
        elif name == "textstream":

            self.src = attrs.get("src", "")
            self.region = attrs.get("region", "")
            self.all.append({"name": name, "src": self.src, "region": self.region})

    def get_tags(self):

        return self.all




if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    all = cHandler.get_tags()
    print(all)
