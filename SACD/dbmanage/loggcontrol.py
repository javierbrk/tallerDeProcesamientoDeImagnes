import logging
import time
import datetime
import sys
try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    sys.path.append('../')
    from inference_engine.var import cwd, sys_name
except:
    pass

if 'sys_name' in globals():
    fia = sys_name
else:
    fia = ""

_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


LOG_FILENAME = '{}\log_app.log'.format(cwd)
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


def logg(text):
    logging.debug("{}:{}".format(_now, text))
    return 1

class sv_obj2dat(object):
    def _init_(self, _obj, _file):
        self.obj = _obj
        try:
            self.file = _file
        except NameError:
            self.file=file("datos.dat", "w")
    def sv(self):
        pickle.dump(self.obj, self.file)
        self.file.close()
