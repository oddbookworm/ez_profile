import atexit
from os import popen
import sys

from . import profiler

try:
    import snakeviz

    sv = True
except ImportError:
    print("snakeviz not found, will not display output in browser")
    sv = False


def handle_exit():
    profiler.on_exit()

    if sv:
        print("Displaying result in browser. Ctrl-C when finished.")
        proc = popen("{} -m snakeviz stats.prof".format(sys.executable))
        proc.read()
        proc.close()

    else:
        profiler.profiler.print_stats()


atexit.register(handle_exit)
