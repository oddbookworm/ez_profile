import atexit
from os import popen

try:
    import snakeviz
    sv = True
except ImportError:
    print("snakeviz not found, will not display output in browser")
    sv = False

from . import profiler

def handle_exit():
    profiler.on_exit()

    if sv:
        print("Displaying result in browser. Ctrl-C when finished.")
        proc = popen('python -m snakeviz stats.prof')
        proc.read()
        proc.close()
        
    else:
        profiler.profiler.print_stats()

atexit.register(handle_exit)