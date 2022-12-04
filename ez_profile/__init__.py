from sys import argv
if "--ignore" not in argv:
    from os import popen
    import sys
    #from . import snakeviz_launcher

    print(f'Running command: "{sys.executable}" -m cProfile -o stats.prof "{argv[0]}" --ignore')
    proc = popen(f'"{sys.executable}" -m cProfile -o stats.prof "{argv[0]}" --ignore')
    print(proc.read())
    proc.close()

    print("launching snakeviz. Ctrl-C to close")
    print(f'Running command: "{sys.executable}" -m snakeviz stats.prof')
    proc = popen(f'"{sys.executable}" -m snakeviz stats.prof')
    proc.read()
    proc.close()

    quit()
