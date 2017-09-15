import re
import os
from string import Template
from pprint import pprint
from moduleStruct import splitFile,originModule

MODULE_TMP = Template('''module ${module_name} #(\n${module_parameter})
(${module_inout});
${module_localparam}
${module_wire}
${module_reg}
${module_assign}
${module_always}
${module_call}
endmodule''')

def genByload(path):
    _modstruct = {}
    modulelist = splitFile(path)
    for mod in modulelist:
        _temp = originModule(mod)
        if _temp.DB_modulename is not None:
            _modstruct[_temp.DB_modulename] = _temp
        else:
            pass
    for name in _modstruct:
        _file = open(name+'.v','w')
        _file.write(MODULE_TMP.substitute(module_name = name,
                                          module_parameter = _modstruct[name].showParameter(),
                                          module_inout = _modstruct[name].showInout(),
                                          module_localparam = _modstruct[name].showLocalparam(),
                                          module_reg = _modstruct[name].showReg(),
                                          module_wire = _modstruct[name].showWire(),
                                          module_assign = '',
                                          module_always = _modstruct[name].showAlways(),
                                          module_call = ''
                                          ))
        _file.close()

def genByinfo(modulename='default',**arg):
    modByinfo = originModule()
    modByinfo.DB_modulename = modulename
    modByinfo.DB_para = arg.get('dbpara',{})
    modByinfo.DB_lp = arg.get('dblp',{})
    modByinfo.DB_input = arg.get('dbin',{})
    modByinfo.DB_output = arg.get('dbout',{})
    modByinfo.DB_inout = arg.get('dbio',{})
    modByinfo.DB_reg = arg.get('dbreg',{})
    modByinfo.DB_wire = arg.get('dbwire',{})
    
    _file = open(modByinfo.DB_modulename+'.v','w')
    _file.write(MODULE_TMP.substitute(module_name = modByinfo.DB_modulename,
                                          module_parameter = modByinfo.showParameter(),
                                          module_inout = modByinfo.showInout(),
                                          module_localparam = modByinfo.showLocalparam(),
                                          module_reg = modByinfo.showReg(),
                                          module_wire = modByinfo.showWire(),
                                          module_assign = '',
                                          module_always = '',
                                          module_call = ''
                                          ))
    _file.close()

##file = open('E:/pythonwork/veriGen1.1/countspeed.v')
##temp = originModule(file.read())
##genByinfo(dbpara=temp.DB_para,
##          dblp=temp.DB_lp,
##          dbin=temp.DB_input,
##          dbout=temp.DB_output,
##          dbio=temp.DB_inout,
##          dbreg=temp.DB_reg,
##          dbwire=temp.DB_wire)
