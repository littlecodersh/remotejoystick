'''
Usage:
    remotejoystick -e -p PORT [-n COUNT]
    remotejoystick -s -d ADDRESS -p PORT [-c CODE] [-j STICKINDEX]
    remotejoystick -r -d ADDRESS -p PORT [-c CODE]
    remotejoystick (-l | --local)
    remotejoystick (-h | --help)
    remotejoystick --version

Options:
    -h --help       show this screen
    -v --version    show version
    -l --local      use joystick as keyboard locally
    -e --server     start as server
    -s --sender     start as sender
    -r --receiver   start as receiver
    -d ADDRESS      specify ip address of server
    -p PORT         specify port for server [default: 6320]
    -n COUNT        specify pairs accept (only for server) [default: 1]
    -c CODE         specify verify code for receiver & sender [default: ab12]
    -j STICKINDEX   specify joystick index for input [default: 0]
'''
from docopt import docopt
from __init__ import __version__ as version

def main():
    arg = docopt(__doc__, version=version)
    arg['-p'], arg['-n'] = int(arg['-p']), int(arg['-n'])
    if arg['--server']:
        from server import run_server
        run_server(arg['-p'], arg['-n'])
    elif arg['--sender']:
        from sender import run_sender
        run_sender(arg['-d'], arg['-p'], arg['-c'], arg['-j'])
    elif arg['--receiver']:
        from receiver import run_receiver
        run_receiver(arg['-d'], arg['-p'], arg['-c'])
    elif arg['--local']:
        from local import run_local
        run_local(arg['-c'])
    print('Bye~')

if __name__ == '__main__':
    main()
