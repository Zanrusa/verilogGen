import re

from pprint import pprint
from string import Template

DICT_VALUE = {
    'r':'reg',
    'w':'wire',
    'i':'input',
    'o':'output',
    'b':'inout',
    'p':'parameter',
    'l':'localparam',
    'd':'define'
    }
DICT_KEY = {
    v:k for k,v in DICT_VALUE.items()
    }

RE_LP = re.compile(r'\s*localparam\s+([a-zA-Z0-9_]+)\s*=\s*([bhd0-9\'_]+)\s*;\s*')

RE_PARA = re.compile(r'\s*parameter\s+([a-zA-Z0-9_]+)\s*=\s*([bhd0-9\'_]+)\s*,{0,1}\s*')

RE_WIRE = re.compile(r'\s*(?P<iotype>output|input|inout)?(?(iotype)\s+(wire){0,1}|wire)\s*(\[.+\]){0,1}\s*([A-Za-z0-9_]+)\s*(=\s*([bhd0-9\'_]+)){0,1}\s*[;,]{0,1}\s*')

RE_REG = re.compile(r'\s*(output\s+){0,1}reg\s+(\[.+\]){0,1}\s*([a-zA-Z0-9_]+)\s*(=\s*([bhd0-9\'_]+)){0,1}\s*[,;]{0,1}\s*')

WIRE_WIDTH = re.compile(r'\[.*:')
WIRE_VALUE = re.compile(r"([0-9]*'[bhd])[0-9_]+")
WIRE_OTHER = re.compile(r'[A-Za-z_][A-Za-z0-9_]+')

REG_WIDTH = re.compile(r'\[.*:')
REG_VALUE = re.compile(r"([0-9]*'[bhd])[0-9_]+")
REG_OTHER = re.compile(r'[A-Za-z_][A-Za-z0-9_]+')

def removeDupstr(string,pattern):
    _stringlist = list(string)
    _stringout = ''
    for word in _stringlist:
        if word is not pattern:
            _stringout += word
    return _stringout+pattern

class originType(object):
    def __init__(self,iname,itype,iwidth,ivalue):
        self.getName = iname
        self.getType = itype
        self.getWidth = iwidth
        self.getValue = ivalue

    def widthDeal(self,pattern=r'.*',string=''):
        _searchres = re.search(pattern,string)
        _result = _searchres.group() if _searchres else '0'
        return _result
        

    @property
    def getName(self):
        return self._name
    @getName.setter
    def getName(self,iname):
        self._name = iname

    @property
    def getType(self):
        return self._type
    @getType.setter
    def getType(self,itype):
        self._type = itype

    def fullType(self):
        _typelist = []
        for types in self.getType:
            _typelist.append(DICT_VALUE[types])
        return _typelist

    @property
    def getWidth(self):
        return self._width
    @getWidth.setter
    def getWidth(self,iwidth):
        self._width = int(iwidth)

    def fullWidth(self):
        return '['+str(self.getWidth)+':0]'

    @property
    def getValue(self):
        return self._value
    @getValue.setter
    def getValue(self,ivalue):
        self._value = ivalue

    @property
    def getDescripter(self):
        raise IOError('origin type is not available!')
    @getDescripter.setter
    def getDescripter(self,idescripter):
        raise IOError('origin type is not available!')
    

class defineType(originType):
    def __init__(self,iname,ivalue):
        self.getName = iname
        self.getType = 'd'
        self.getValue = ivalue
    
    @property
    def getWidth(self):
        raise IOError('define type has no width!')
    @getWidth.setter
    def getWidth(self,iwidth):
        raise IOError('define type has no width!')

    def fullWidth(self):
        raise IOError('define type has no width!')

    def callName(self):
        return '`'+self.getName

    @property
    def getDescripter(self):
        _descripter = '`define\t'+self.getName +str(self.getValue)
        return _descripter
    @getDescripter.setter
    def getDescripter(self,idescripter):
        elelist = re.split(r'\s+',idescripter)
        self.getName = elelist[1]
        self.getValue= elelist[2]
        

class lpType(originType):

    def __init__(self,iname='',ivalue=''):
        self.getName = iname
        self.getType = 'l'
        self.getValue = ivalue

    @property
    def getWidth(self):
        raise IOError(DICT_VALUE[self.getType]+'type has no width!')
    @getWidth.setter
    def getWidth(self,iwidth):
        raise IOError(DICT_VALUE[self.getType]+'type has no width!')

    def fullWidth(self):
        raise IOError(DICT_VALUE[self.getType]+'type has no width!')

    @property
    def getDescripter(self):
        return  'localparam\t'+self.getName + '\t=\t'+str(self.getValue)
    @getDescripter.setter
    def getDescripter(self,idescripter):
        elelist = re.split(r'\s*=*\s*',idescripter)
        self.getName = elelist[1]
        self.getValue= elelist[2].rstrip(';')
    

class paraType(lpType):
    
    def __init__(self,iname='',ivalue=''):
        self.getName = iname
        self.getType = 'p'
        self.getValue = ivalue

    def callinModule(self):
        return '.'+self.getName+'(),\n'

    @property
    def getDescripter(self):
        return  'parameter\t'+self.getName + '\t=\t'+str(self.getValue) 
    @getDescripter.setter
    def getDescripter(self,idescripter):
        elelist = re.split(r'\s*=*\s*',idescripter)
        self.getName = elelist[1]
        self.getValue= elelist[2]
    
class wireType(originType):

    def __init__(self,iname='default',itype='w',iwidth='12',ivalue='4\'b1000'):
        super().__init__(iname=iname,itype=removeDupstr(itype,'w'),iwidth=iwidth,ivalue=ivalue)

    def callinModule(self):
        return '.'+self.getName+'(),\n'


    @property
    def getDescripter(self):
        _descripter = ''
        for types in self.fullType():
            if types is 'wire':
                _descripter = _descripter +  types +'\t'
            else:
                _descripter = types +'\t'+ _descripter
        _descripter =_descripter + self.fullWidth() + '\t'+self.getName
        return _descripter
    @getDescripter.setter
    def getDescripter(self,idescripter=''):
        self.getWidth = self.widthDeal(WIRE_WIDTH,idescripter).strip(' \t[:')
        self.getValue = '0'if not WIRE_VALUE.search(idescripter)else WIRE_VALUE.search(idescripter).group()
        templist = WIRE_OTHER.findall(idescripter.split('=')[0])
        self.getType=''.join([DICT_KEY.get(word,'') for word in templist])
        if 'w' not in self.getType:
            self.getType += 'w'
        self.getName = templist[-1]

class regType(originType):
    
    def __init__(self,iname='default',itype='r',iwidth='12',ivalue='4\'b1000'):
        super().__init__(iname=iname,itype=removeDupstr(itype,'r'),iwidth=iwidth,ivalue=ivalue)

    def callinModule(self):
        return '.'+self.getName+'(),\n'

    @property
    def getDescripter(self):
        _descripter = ''
        for types in self.fullType():
            if types is 'reg':
                _descripter = _descripter +  types +'\t'
            else:
                _descripter = types +'\t'+ _descripter
        _descripter =_descripter + self.fullWidth() + '\t'+self.getName
        return _descripter
    @getDescripter.setter
    def getDescripter(self,idescripter=''):
        self.getWidth = self.widthDeal(REG_WIDTH,idescripter).strip(' \t[:')
        self.getValue = '0'if not REG_VALUE.search(idescripter)else REG_VALUE.search(idescripter).group()
        templist = REG_OTHER.findall(idescripter.split('=')[0])
        self.getType=''.join([DICT_KEY.get(word,'') for word in templist])
        self.getName = templist[-1]
        

def judgeType(idescripter='',**arg):
##    print(arg.get('itype',''))
    if re.fullmatch(RE_WIRE,idescripter):
##        print('wire type by des')
        _judgetype = wireType()
        _judgetype.getDescripter = idescripter
    elif re.fullmatch(RE_REG,idescripter):
##        print('reg type by des')
        _judgetype = regType()
        _judgetype.getDescripter = idescripter
    elif re.search(r'r',arg.get('itype','')):
##        print('reg type by __init__')
        _judgetype = regType(iname=arg.get('iname',''),
                             itype=arg.get('itype',''),
                             iwidth=arg.get('iwidth',''),
                             ivalue=arg.get('ivalue',''))
    elif re.search(r'w',arg.get('itype','')):
##        print('wire type by __init__')
        _judgetype = wireType(iname=arg.get('iname',''),
                             itype=arg.get('itype',''),
                             iwidth=arg.get('iwidth',''),
                             ivalue=arg.get('ivalue',''))
    else:
        _judgetype =None
    return _judgetype
