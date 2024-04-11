'''
///////////////////////////////////YUNYOO.CN////////////////////////////////////
//                                                                             *
// VMPStudio PLUGIN PYTHON INTERFACE FILE                                      *
//                                                                             *
// Copyright(C) 2022 YunYoo Corp., ALL RIGHTS RESERVED.                        *
//                                                                             *
// Internet: yunyoo.cn                                                         *
//                                                                             *
// This code is distributed "as is", part of VMPStudio and without warranty of *
// any kind, expressed or implied, including, but not limited to warranty of   *
// fitness for any particular purpose. In no event will VMPStudio be liable to *
// you for any special, incidental, indirect, consequential or any other       *
// damages caused by the use, misuse, or the inability to use of this code,    *
// including anylost profits or lost savings,even if VMPStudio has been advised*
// of the possibility of such damages.                                         *
//                                                                             *
///////////////////////////////////////*////////////////////////////////////////
'''

import _vsp
import importlib
from vspdef import *

# current version
vspy_version = '1.0.0'

# entry for api
def api_proc(name, args = None):
    """
    internal use.
    """
    if args is None:
        return _vsp.vsp_entry({'action':'api', 'name':name})
    return _vsp.vsp_entry({'action':'api', 'name':name, 'args':args})

def api_proc_result(api, args = None):
    """
    internal use.
    """
    result = api_proc(api, args)
    err = result[vsp_outkey_error]
    if err != vsp_err_ok:
        print('API %s(%s) return an error: %d.' % (api, args, err))
        return None
    return result[vsp_outkey_result]

# api interface

# void (*logStatus)(const char *msg)
def logStatus(msg):
    """
    print the string msg to status bar.
    """
    api_proc('logStatus', msg)

# void (*gotoCPUAddress)(vspint addr)
def gotoCPUAddress(addr):
    """
    make cpu disassembly widget go to address.
    """
    api_proc('gotoCPUAddress', addr)

def cpu(addr):
    """
    wrapper for gotoCPUAddress.
    """
    return gotoCPUAddress(addr)

# void (*gotoTraceAddress)(vspint addr)
def gotoTraceAddress(addr):
    """
    make uvmse trace window go to address.
    """
    api_proc('gotoTraceAddress', addr)

# vsp_error_t (*getModule)(vsp_module_t *module)
def getModule():
    """
    get the loaded module information.
    """
    return api_proc_result('getModule')

# void (*travelFunc)(vsp_error_t (*handler)(const vsp_func_t *func))
def travelFunc(handler):
    """
    iterate all the function in the module.
    a sample handler:
    def handler(func):
        print(func)
        return vsp_err_continue
    the function callback argument is a dict object.
    """
    api_proc('travelFunc', handler)

# vspint (*hasModule)()
def hasModule():
    """
    check whether has loaded module.
    """
    return api_proc_result('hasModule')

# vsp_error_t (*readBytesFoff)(vspint foff, void *buff, vspint size)
def readBytesFoff(foff, size):
    """
    read module bytes with file offset.
    """
    return api_proc_result('readBytesFoff', (foff, size))

# vsp_error_t (*readBytesAddr)(vspint addr, void *buff, vspint size)
def readBytesAddr(addr, size):
    """
    read module bytes with address.
    """
    return api_proc_result('readBytesAddr', (addr, size))

# vsp_error_t (*gotoDumpAddress)(vspint addr, vspint index)
def gotoDumpAddress(addr, index):
    """
    make dump window goto the specified address, index range [0, 4].
    """
    return api_proc_result('gotoDumpAddress', (addr, index))

def dump(addr, index = 0):
    """
    wrapper for gotoDumpAddress.
    """
    return gotoDumpAddress(addr, index)

# vsp_error_t (*getIntConfig)(const char *sect, const char *key, vspint *value)
def getIntConfig(sect, key):
    """
    get an integer config from VMPStudio.ini.
    """
    return api_proc_result('getIntConfig', (sect, key))

# vsp_error_t (*getConfig)(const char *sect, const char *key, char *cfg,
#                           vspint cfgsize)
def getConfig(sect, key):
    """
    get a string config from VMPStudio.init.
    """
    return api_proc_result('getConfig', (sect, key))

# vsp_error_t (*setIntConfig)(const char *sect, const char *key, vspint value)
def setIntConfig(sect, key, value):
    """
    set an integer config to VMPStudio.init.
    """
    return api_proc_result('setIntConfig', (sect, key, value))

# vsp_error_t (*getConfig)(const char *sect, const char *key, const char *cfg)
def setConfig(sect, key, value):
    """
    set a string config to VMPStudio.init.
    """
    return api_proc_result('setConfig', (sect, key, value))

# vsp_error_t (*inputString)(const char *title, char *text, vspint size)
def inputString(title):
    """
    show a string input dialog.
    """
    return api_proc_result('inputString', title)

# vsp_error_t (*inputInteger)(const char *title, vspint *value)
def inputInteger(title):
    """
    show an integer input dialog.
    """
    return api_proc_result('inputInteger', title)

# vsp_error_t (*inputPath)(char *path, vspint size, vspint isdir,
#                          vspint isopen)
def inputPath(isdir = False, isopen = True):
    """
    show a dir/file open/save dialog.
    """
    return api_proc_result('inputPath', (isdir, isopen))

# vsp_error_t (*disassemble)(const void *opcode, char *asmcode, vspint asmsize)
def disassemble(opcode):
    """
    disassemble the opcode to string. opcode should be a bytes object.
    """
    return api_proc_result('disassemble', opcode)

def disas(opcode):
    """
    wrapper for disassemble.
    """
    return disassemble(opcode)

def disasint(opcode):
    """
    disassemble the opcode to string, opcode should be an integer object.
    """
    return api_proc_result('disassembleFromInteger', opcode)

# vsp_error_t (*assemble)(const char *asmcode, void *opcode)
def assemble(asmcode):
    """
    assemble the string asmcode to machine opcode, the result is a bytes object.
    """
    return api_proc_result('assemble', asmcode)

def asm(asmcode):
    """
    wrapper for assemble.
    """
    return assemble(asmcode)

def asmint(asmcode):
    """
    assemle the string asmcode to machine opcode, the result is an integer object.
    """
    return api_proc_result('assembleToInteger', asmcode)

# vsp_error_t (*setUVMBreakpoint)(vspint addr)
def setUVMBreakpoint(addr):
    """
    set a uvm breakpoint at addr.
    """
    api_proc('setUVMBreakpoint', addr)

def uvmbp(addr):
    """
    set a uvm breakpoint at addr.
    """
    return setUVMBreakpoint(addr)

# vsp_error_t (*unsetUVMBreakpoint)(vspint addr);
def unsetUVMBreakpoint(addr):
    """
    remove the uvm breakpoint at addr.
    """
    api_proc('unsetUVMBreakpoint', addr)

# vsp_error_t (*getSampleDatabase)(vsp_sdb_t *sdb)
def getSampleDatabase():
    """
    get current sample database information.
    """
    return api_proc_result('getSampleDatabase')

# vsp_error_t (*getTrackIndexs)(vspint i, const vspint **indexs, vspint *size)
def getTrackIndexs(index):
    """
    get trace track pc indexs at index.
    """
    return api_proc_result('getTrackIndexs', index)

def getTrackIndexsValue(handle, index):
    """
    get trace track pc indexs value at index
    """
    return api_proc_result('getTrackIndexsValue', (handle, index))

# vsp_error_t (*getRecordInfo)(vspint addr, const void **handle, vspint *size)
def getRecordInfo(addr):
    """
    get register record handle and count at address.
    """
    return api_proc_result('getRecordInfo', addr)

# vsp_error_t (*getRegister)(const void *handle, vspint index, const char *regname, vspint *regvalue)
def getRegister(handle, index, regname):
    """
    pickup register value with name at index for given handle.
    regname {
        arm: r0-r14, fp, lr, sp, flags
        arm64: x0-x30, fp, lr, flags
        x86/x86_64: rax, rbx, rcx, rdx, rbp, rdi, rsi, rsp, r8-r15, flags
    }
    """
    return api_proc_result('getRegister', (handle, index, regname))

# vsp_error_t (*getRegisterWithIndex)(const void *handle, vspint index, vspint regidx, vspint *regvalue)
def getRegisterWithIndex(handle, index, regidx):
    """
    pickup register value with regindex at index for given handle.
    regidx {
        arm: [0, 14]
        arm64: [0, 30]
        x86/x86_64: [0, 15]
    }
    """
    return api_proc_result('getRegisterWithIndex', (handle, index, regidx))   

# vsp_error_t (*getMemoryPage)(vspint addr, vspint *pageaddr, const char **pagebuff, vspint *pagesize)
def getMemoryPage(addr):
    """
    pickup runtime address memory page information and buffer
    """
    return api_proc_result('getMemoryPage', addr) 

# vsp_error_t (*command)(const char *cmd)
def command(cmd):
    """
    execute a remote shell command without result.
    """
    return api_proc('command', cmd)

# vsp_error_t (*commandResult)(const char *cmd, char *result, vspint size)
def commandResult(cmd):
    """
    execute a remote shell command, return the string output.
    """
    return api_proc_result('commandResult', cmd)

# vspint (*registerCommander)(const char *name,
#                             bool (*handler)(const char *cmd))
def registerCommander(name, handler):
    """
    register your own commander to the command edit, a sample handler:
    def handler(cmds):
        print('(VMPStudio vsp) %s' % (cmds))
        return True
    the result is the commander id, pass it to unregisterCommander to remove it.
    """
    return api_proc_result('registerCommander', (name, handler))

# void (*unregisterCommander)(vspint idval)
def unregisterCommander(idval):
    """
    remove the commander with id, idval is returned by registerCommander.
    """
    api_proc('unregisterCommander', idval)

# void (*attach)(vspint pid)
def attach(pid):
    """
    attach to the process with pid to sample function with uraniumvm.
    """
    api_proc('attach', pid)

# void (*detach)()
def detach():
    """
    detach from current samplee.
    """
    api_proc('detach')

# open a file to analyze or a python script to exeucte with its full path
def open(path):
    command('init "%s"' % (path))

# python expression or path
def runPython(py):
    """
    run a python expression or script file.
    """
    api_proc('runPython', py)

def runpy(py):
    """
    wrapper for runPython.
    """
    return runPython(py)
    
# vsp_file_t (*curFileType)();
def curFileType():
    return api_proc_result('curFileType')

# vsp_arch_t (*curArchType)();
def curArchType():
    """
    return the current debugee arch, like:
    vsp_arch_arm = 2
    vsp_arch_arm64 = 3
    vsp_arch_x86 = 4
    vsp_arch_x64 = 5
    """
    return api_proc_result('curArchType')

# event result wrapper
def vsp_result(err, value = None):
    """
    the vsp event callback should use this function to construct the result.
    """
    if value is None:
        return {vsp_outkey_error:err}
    return {vsp_outkey_error:err, vsp_outkey_result:value}

def success(value = None):
    """
    the vsp event callback success result.
    """
    return vsp_result(vsp_err_ok, value)

def failed(err = vsp_err_failed):
    """
    the vsp event callback failure result.
    """
    return vsp_result(err)

# internal python plugin instance
usrvsp = {}

# internal used event callback for vsp python3 module
def vsp_on_event(args):
    global usrvsp
    # get user plugin module name
    name = args[vsp_inkey_name]
    if name is None:
        return vsp_result(vsp_err_notfound)
    # get user plugin module
    module = usrvsp.get(name)
    if module is None:
        # import user plugin module
        module = importlib.import_module(name)
        if module is None:
            return vsp_result(vsp_err_failed)
        usrvsp[name] = module
    # pre-process event
    event = args[vsp_inkey_type]
    if event == vsp_event_version:
        return vsp_result(vsp_err_ok, vsp_version)
    # invoke user plugin's event handler
    handler = module.vsp_on_event
    if handler is None:
        return vsp_result(vsp_err_unimpl)
    # pass event to user plugin's handler
    return handler(args)
