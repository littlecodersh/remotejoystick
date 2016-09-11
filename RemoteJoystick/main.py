'''
Usage:
    remote-joystick (-e | -s | -r) [-d ADDRESS] [-p PORT] [-n COUNT] [-c CODE]
    remote-joystick (-l | --local)
    remote-joystick (-h | --help)
    remote-joystick --version

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
        run_sender(arg['-d'], arg['-p'], arg['-c'])
    elif arg['--receiver']:
        from receiver import run_receiver
        run_receiver(arg['-d'], arg['-p'], arg['-c'])
    elif arg['--local']:
        from local import run_local
        run_local()
    print('Bye~')

if __name__ == '__main__':
    main()
