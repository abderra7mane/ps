import cmd
try:
    import readline
except:
    pass
import pscore

class PsCmd(cmd.Cmd):

    prompt = "(Ps) "
    
    def do_ls(self, args):
        """List all process"""
        proc_list = pscore.ps_list()
        print "Process ID\tProcess name\n"
        for proc in proc_list:
            print "%-10d\t%s" % (proc['pid'], proc['name'])
    
    do_list = do_ls
    do_dir = do_ls

    def do_exit(self, args):
        """Terminate the application"""
        return True

    do_quit = do_exit

    def emptyline(self):
        return False


def cmd_launcher():
    cmd = PsCmd()
    try:
        cmd.cmdloop()
    except KeyboardInterrupt:
        print "\nCtrl-C captured. terminating"
        return 1
    return 0
