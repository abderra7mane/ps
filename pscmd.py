import cmd
try:
    import readline
except:
    pass
import psutil

class PsCmd(cmd.Cmd):

    prompt = "(Ps) "
    
    def do_ls(self, args):
        """List all process"""
        proc_list = psutil.process_iter(attrs=['name', 'pid'])
        print "Process ID\tProcess name\n"
        for proc in proc_list:
            print "%-10d\t%s" % (proc.info['pid'], proc.info['name'])
    
    do_list = do_ls
    do_dir = do_ls

    def do_exit(self, args):
        """Terminate the application"""
        return True

    do_quit = do_exit

    def emptyline(self):
        return False
