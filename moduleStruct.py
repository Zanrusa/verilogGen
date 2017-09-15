from moduleType import originType,judgeType,lpType,paraType,wireType,regType,DICT_VALUE,DICT_KEY,RE_LP,RE_PARA,RE_WIRE,RE_REG
from string import Template
from pprint import pprint
from collections import OrderedDict 
import re
import os
import sys
import shutil



ALWAYS_BLOCK = re.compile(r'''always(?:(?!begin)(?!end)[\s\S])+begin(?:(?!end)(?!begin)[\s\S])+(?:begin(?:(?!end)(?!begin)[\s\S])+end(?:(?!end)(?!begin)[\s\S])+)*end\s*''')
RE_VFILE = re.compile(r'\w+\.v')
MODULE_TYPE = re.compile(r"module(?:(?!module)(?!endmodule)[\s\S])+endmodule")

class originStruct(object):
    fullstrt = []
    def __init__(self,iname=[],itype=[],iwidth=[],ivalue=[]):
        self.fullstrt = []
        self.strtName = iname
        self.strtType = itype
        self.strtValue = ivalue

    @property
    def strtName(self):
        return self._name
    @strtName.setter
    def strtName(self,iname):
        self._name = iname

    @property
    def strtType(self):
        return self._type
    @strtType.setter
    def strtType(self,itype):
        self._type = itype

    def strtType(self):
        _typelist = []
        for types in self.getType:
            _typelist.append(DICT_VALUE[types])
        return _typelist

    @property
    def strtWidth(self):
        return self._width
    @strtWidth.setter
    def strtWidth(self,iwidth):
        self._width = iwidth

    def fullstrtWidth(self):
        _fullstrtwidth = []
        for num in range(len(self.strtWidth)):
            _fullstrtwidth.append('['+str(self.strtWidth[num])+':0]')
        return _fullstrtwidth
    
    @property
    def strtValue(self):
        return self._value
    @strtValue.setter
    def strtValue(self,ivalue):
        self._value = ivalue

    @property
    def strtDescripter(self):
        raise IOError('origin type is not available!')
    @strtDescripter.setter
    def strtDescripter(self,idescripter):
        raise IOError('origin type is not available!')

class lpStruct(originStruct):
    def __init__(self,ilptype=[]):
        super().__init__()
        self.fullstrt = ilptype
        for num in range(len(ilptype)):
            self.strtName.append(ilptype[num].getName)
            self.strtType.append('l')
            self.strtValue.append(ilptype[num].getValue)

    @property
    def strtWidth(self):
        raise IOError(DICT_VALUE[self.fullstrt[0].getType]+' type has no width!')
    @strtWidth.setter
    def strtWidth(self,iwidth):
        raise IOError(DICT_VALUE[self.fullstrt[0].getType]+' type has no width!')

    def fullstrtWidth(self):
        raise IOError(DICT_VALUE[self.fullstrt[0].getType]+' type has no width!')

    @property
    def strtDescripter(self):
        _descripter = ''
        for strt in self.fullstrt:
            _descripter += strt.getDescripter +';\n'
        return _descripter
    @strtDescripter.setter
    def strtDescripter(self,istrt):
        _lplist = re.split(r'\n\s*',istrt)
        self.fullstrt = []
        for lp in _lplist:
            if RE_LP.fullmatch(lp):
                _temp = lpType()
                _temp.getDescripter = lp
                self.fullstrt.append(_temp)
        for strt in self.fullstrt:
            self.strtName.append(strt.getName)
            self.strtType.append(strt.getType)
            self.strtValue.append(strt.getValue)

class paraStruct(lpStruct):
    def __init__(self,iparatype=[]):
        super().__init__()
        self.fullstrt = iparatype
        for num in range(len(iparatype)):
            self.strtName[num] = iparatype[num].getName
            self.strtType[num] = 'p'
            self.strtValue[num] = iparatype[num].getValue

    def callStruct(self):
        _call = ''
        for strt in self.fullstrt:
            _call += strt.callinModule()+'\n'
        _result='#(\n'+_call.rstrip('\n,')+')'
        return _result

    @property
    def strtDescripter(self):
        _descripter = ''
        for strt in self.fullstrt:
            _descripter += strt.getDescripter +',\n'
        return _descripter
    @strtDescripter.setter
    def strtDescripter(self,istrt):
        _paralist = re.split(r'\n\s*',istrt)
        self.fullstrt = []
        for para in _paralist:
            if RE_PARA.fullmatch(para.strip(',()')):
                _temp = paraType()
                _temp.getDescripter = para.strip(',()')
                self.fullstrt.append(_temp)
        for strt in self.fullstrt:
            self.strtName.append(strt.getName)
            self.strtType.append(strt.getType)
            self.strtValue.append(strt.getValue)

class mainStruct(originStruct):
    def __init__(self,imaintype=[]):
        super().__init__()
        self.strtWidth=[]
        self.fullstrt = imaintype
        for num in range(len(imaintype)):
            self.strtType[num] = imaintype[num].getType
            self.strtName[num] = imaintype[num].getName
            self.strtWidth[num] = imaintype[num].getWidth
            self.strtValue[num] = imaintype[num].getValue

    def callStruct(self):
        _call = ''
        for strt in self.fullstrt:
            _call += strt.callinModule()+'\n'
        return _call
    
    @property
    def strtDescripter(self):
        _descripter = ''
        for strt in self.fullstrt:
            _descripter += strt.getDescripter +'\n'
        return _descripter
    @strtDescripter.setter
    def strtDescripter(self,istrt):
        _mainlist = re.split(r'\n\s*',istrt.strip(' \t\n'))
        self.fullstrt = []
        for element in _mainlist:
            _temp = judgeType(element.strip('();'))
            if _temp:
                self.fullstrt.append(_temp)
            else:
                pass
        self.strtName =[]
        self.strtType =[]
        self.strtWidth =[]
        self.strtValue =[]
        for strt in self.fullstrt:
            self.strtName.append(strt.getName)
            self.strtType.append(strt.getType)
            self.strtWidth.append(strt.getWidth)
            self.strtValue.append(strt.getValue)

def splitFile(path='*.v'):
        if not RE_VFILE.match(os.path.basename(path)):
            return None
        else:
            vfile=open(path,'r')
        vcontent = vfile.read()
        modulelist =MODULE_TYPE.findall(vcontent)
        return modulelist
    
class originModule(object):
    DB_modulename = ''
    DB_para = {}
    DB_lp = {}
    DB_input = {}
    DB_output = {}
    DB_inout = {}
    DB_reg = {}
    DB_wire = {}
    DB_always = {}

    def __init__(self,iModule=''):
        self.DB_para ={}
        self.DB_lp = {}
        self.DB_input = {}
        self.DB_output = {}
        self.DB_inout = {}
        self.DB_reg = {}
        self.DB_wire = {}
        self.DB_always = {}
        if MODULE_TYPE.match(iModule):
            self.DB_modulename = re.search(r'(?<=^module)\s+([A-Za-z0-9_]+)\b',iModule).group(1)
            self.findAlways(iModule=iModule)
            self.findLocalparam(iModule=iModule)
            self.findParameter(iModule=iModule)
            self.findPort(iModule=iModule)

    def findAlways(self,iModule):
        _alwaysblock =  ALWAYS_BLOCK.findall(iModule)
        if _alwaysblock:
            for num in range(len(_alwaysblock)):
                self.DB_always[num] = _alwaysblock[num]
            return self.DB_always
        else:
            return None

    def findLocalparam(self,iModule):
        _ls = lpStruct()
        _ls.strtDescripter = iModule
        for lt in _ls.fullstrt:
            self.DB_lp[lt.getName] = lt
        return self.DB_lp

    def findParameter(self,iModule):
        _ps = paraStruct()
        _ps.strtDescripter = iModule
        for pt in _ps.fullstrt:
            self.DB_para[pt.getName] = pt
        return self.DB_para

    def findPort(self,iModule):
        _ms = mainStruct()
        _ms.strtDescripter = iModule
        for mt in _ms.fullstrt:
            if re.search(r'i',mt.getType):
                self.DB_input[mt.getName] = mt
            elif re.search(r'o',mt.getType):
                self.DB_output[mt.getName] = mt
            elif re.search(r'b',mt.getType):
                self.DB_inout[mt.getName] = mt
            elif re.search(r'r',mt.getType):
                self.DB_reg[mt.getName] = mt
            else:
                self.DB_wire[mt.getName] = mt
        return True

    def showParameter(self):
        self.DB_para = OrderedDict(sorted(self.DB_para.items(),key = lambda x:x[0]))
        _para = paraStruct(list(self.DB_para.values()))
        return _para.strtDescripter.rstrip(',\n')
    
    def showLocalparam(self):
        self.DB_lp = OrderedDict(sorted(self.DB_lp.items(),key = lambda x:x[0]))
        _lp = lpStruct(list(self.DB_lp.values()))
        return _lp.strtDescripter
    
    def showInout(self):
        _inouttext = ''
        _inputtext = ''
        _outputtext = ''
        self.DB_inout = OrderedDict(sorted(self.DB_inout.items(),key = lambda x:x[0]))
        self.DB_input = OrderedDict(sorted(self.DB_input.items(),key = lambda x:x[0]))
        self.DB_output = OrderedDict(sorted(self.DB_output.items(),key = lambda x:x[0]))
        for name in self.DB_inout:
            _inouttext +=self.DB_inout[name].getDescripter+',\n'
        for name in self.DB_input:
            _inputtext +=self.DB_input[name].getDescripter+',\n'
        for name in self.DB_output:
            _outputtext +=self.DB_output[name].getDescripter+',\n'
        return (_inputtext + _outputtext + _inouttext).rstrip('\n,')


    def showReg(self):
        _regtext = ''
        self.DB_reg = OrderedDict(sorted(self.DB_reg.items(),key = lambda x:x[0]))
        for name in self.DB_reg:
            _regtext +=self.DB_reg[name].getDescripter+';\n'
        return _regtext

    def showWire(self):
        _wiretext = ''
        self.DB_wire = OrderedDict(sorted(self.DB_wire.items(),key = lambda x:x[0]))
        for name in self.DB_wire:
            _wiretext +=self.DB_wire[name].getDescripter+';\n'
        return _wiretext

    def showAlways(self):
        _alwaystext = ''
        for name in self.DB_always:
            _alwaystext += self.DB_always[name] +'\n\n'
        return _alwaystext
        
        
###for testing
##TYPICAL_MOD_DEF = '''module type #(
##parameter a_type = 129,
##parameter b_type=130)(
##input wire [10:0] input_a,
##input [ 1 : 0 ] input_b,
##input input_c,
##output wire [1:0] output_a,
##output reg output_b,
##output reg [3 : 0]output_c,
##output wire output_d,
##input clkin,
##input rst_n);
##
##localparam lp_a = 4'b1010;
##localparam lp_b=5'b01010;
##localparam lp_c = 2'b10;
##localparam lp_d= 150;
##localparam lp_e =20;
##
##reg [10:0] a_mid_reg;
##reg [1:0]b_mid_reg;
##reg c_mid_reg;
##wire [1:0]a_mid_wire;
##wire b_mid_wire;
##
##assign a_mid_wire= input_b;
##assign b_mid_wire = input_c ;
##assign output_d = input_c ;
##
##always @(posedge clkin or negedge rst_n) begin
##    if( ~rst_n ) begin
##    output_c <= 0;
##    end else begin
##    output_c<= output_c+1'b1;
##    end
##end
##
##endmodule'''        
##
##tes = '''module type #(
##parameter a_type = 129,
##parameter b_type=130)(
##input wire [10:0] input_a,
##input [ 1 : 0 ] input_b,
##input input_c,
##output wire [1:0] output_a,
##output reg output_b,
##output reg [3 : 0]output_c,
##output wire output_d,
##input clkin,
##input rst_n);
##
##localparam lp_a = 4'b1010;
##localparam lp_b=5'b01010;
##localparam lp_c = 2'b10;
##localparam lp_d= 150;
##
##always @(posedge clkin or negedge rst_n) begin
##    if( ~rst_n ) begin
##    output_c <= 0;
##    end else begin
##    output_c<= output_c+1'b1;
##    end
##end
##
##endmodule
##
##module type #(
##parameter a_type = 129,
##parameter b_type=130)(
##input wire [10:0] input_a,
##input [ 1 : 0 ] input_b,
##input input_c,
##output wire [1:0] output_a,
##output reg output_b,
##output reg [3 : 0]output_c,
##output wire output_d,
##input clkin,
##input rst_n);
##
##localparam lp_a = 4'b1010;
##localparam lp_b=5'b01010;
##localparam lp_c = 2'b10;
##localparam lp_d= 150;
##
##always @(posedge clkin or negedge rst_n) begin
##    if( ~rst_n ) begin
##    output_c <= 0;
##    end else begin
##    output_c<= output_c+1'b1;
##    end
##end
##
##endmodule'''     
##            
##
##c=originModule(TYPICAL_MOD_DEF)
##print('******************************always block********************************\n')
##pprint(c.DB_modulename)
##print('******************************always block********************************\n')
##pprint(c.DB_always)
##print('******************************localparam**********************************\n')
##lp = c.DB_lp
##for k in lp:
##    print(lp[k].getDescripter)
##print('******************************parameter***********************************\n')
##para = c.DB_para
##for k in para:
##    print(para[k].getDescripter)
##print('******************************reg****************************************\n')
##m = c.DB_reg
##n = c.DB_wire
##for k in m:
##    print(m[k].getDescripter)
##print('******************************wire****************************************\n')
##for k in n:
##    print(n[k].getDescripter)
##print('*****************************others***************************************\n')
##pprint(MODULE_TYPE.findall(''))


