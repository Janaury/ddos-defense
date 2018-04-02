from ControlSocket import ControlSocket
from Config import ConfigWriter

class Click(object):
    '''A click object, including all the information
       about a remote click'''
    online = False
    IPaddr = ''
    controlPort = 11111
    dataPort = 33333
    ddosservice = ['NAT','UDP','syn flood']
    config = 'default config'
    configPath = './config/'

    def __init__(self,name,ipaddr,controlPort,dataPort):
        self.ipaddr = ipaddr
        self.controller = ControlSocket(self)
        self.writer = ConfigWriter(self)
        self.datapipe = None

    def ChangeConfig(self):
        self.writer.write_new_config(controlPort,ddosservice)
        self.controller.HotConfig()