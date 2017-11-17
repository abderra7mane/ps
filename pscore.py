import psutil


def ps_list():
    result = []
    proc_iter = psutil.process_iter(attrs=['name', 'pid', 'status'])
    for proc in proc_iter:
        result.append({
            'pid': proc.info['pid'], 
            'name': proc.info['name'],
            'status': proc.info['status']
        })
    return result
