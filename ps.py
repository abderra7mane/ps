import psutil


proc_iter = psutil.process_iter(attrs=['name', 'pid'])

print "Process ID\tProcess name\n"
for proc in proc_iter:
    print "%-10d\t%s" % (proc.info['pid'], proc.info['name'])
