import sys


def main():
    if len(sys.argv) == 1:
        sys.argv.append('-c')

    if sys.argv[1] == '-c' or sys.argv[1] == '--cmd':
        sys.exit(main_cmd())
    elif sys.argv[1] == '-g' or sys.argv[1] == '--gui':
        sys.exit(main_gui())
    else:
        sys.exit(usage())

def main_cmd():
    import pscmd
    return pscmd.cmd_launcher()

def main_gui():
    import psgui
    return psgui.gui_launcher()

def usage():
    print """
usage : ps.py [-c|--cmd]|[-g|--gui]

-c --cmd    launch in interactive command line
-g --gui    launch the gui interface
"""
    return 0

if __name__ == "__main__":
    main()
