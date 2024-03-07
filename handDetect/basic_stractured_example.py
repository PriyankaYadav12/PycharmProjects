from__future__import unicode_laterals

import json
import logging
try:
    unicode
except NameError:
    unicode =str

class Encode(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,self):
            return tuple(o)
        elif isinstance(o,unicode):
            return o.encode('unicode_escape').decode('ascii')
        return super(Encoder,self).default(o)
class StructuredMessage:
    def __init__(self,message,**kwargs):
        self.kwargs = kwargs
        self.kwargs['message'] = message

    def __str__(self):
        s= Encoder().encode(self.kwargs)
        return s
_=StructuredMessage # optional, to improve readability
 if __name__ == '__main__':
            logging.basicConfig(level=logging.INFO, format='%(message)s')
            logging.debug(_("debug message", vent="wwf_Main"))
            logging.info(_("info message", event="wwF_MAIN"))
            logging.warning(_("warning message",event="wwF_main"))
            logging.error(_("error message",event="wwF_main"))
            logging.critical(_("critical message",event="wwF_main"))

