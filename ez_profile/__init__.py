from sys import argv
if "--ignore" not in argv:
    from os import popen
    import sys

    proc = popen(f'"{sys.executable}" -m cProfile -o stats.prof "{argv[0]}" --ignore')
    print(proc.read())
    proc.close()

    print("launching snakeviz. Ctrl-C to close")
    proc = popen(f'"{sys.executable}" -m snakeviz stats.prof')
    proc.read()
    proc.close()

    quit()
