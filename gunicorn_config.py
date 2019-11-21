import multiprocessing

__cpu_count = multiprocessing.cpu_count()

workers = (__cpu_count * 2) + 1
threads = __cpu_count * 3
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %({x-request-id}i)s'
reuse_port = True
preload_app = True
