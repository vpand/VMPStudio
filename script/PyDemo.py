from vspdef import *
from vsp import *

def logger(log):
    print('PyDemo: %s' % (log))

def list_func(func):
    logger(func)
    return vsp_err_continue

logger('hello, world~')

logStatus('PyDemo log to status.\n')

gotoCPUAddress(0)
cpu(0)
gotoTraceAddress(0)
gotoDumpAddress(0, 1)
dump(0)

print('%s' % str(getModule()))
travelFunc(list_func)

logger('has module : %d' % (hasModule()))

logger('bytes at fnoff 0: %s' % str(readBytesFoff(0, 8)))

logger('bytes at address 0: %s' % str(readBytesAddr(0, 8)))

opcode = asmint('nop')
if opcode:
    logger('nop opcode is %d.' % (opcode))
    opcasm = disasint(opcode)
    if opcasm:
        logger('%d disas to %s.' % (opcode, opcasm))

setUVMBreakpoint(0)
uvmbp(0)
unsetUVMBreakpoint(0)

logger('%s' % commandResult('uname -a'))

attach(0)

logger('Current file type %d.' % (curFileType()))
logger('Current arch type %d.' % (curArchType()))

runpy('print("I am a string from python expression string.")')

logger('%s' % (getSampleDatabase()))

logger('%s' % getTrackIndexs(0))
