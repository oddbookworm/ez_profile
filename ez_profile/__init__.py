from sys import argv, exit
if "--ignore" not in argv:
    from subprocess import Popen
    from time import sleep
    import sys
    import signal

    profile_proc = Popen([f'{sys.executable}', '-m', 'cProfile', '-o', 'stats.prof', f'{argv[0]}', '--ignore'], shell=True)
    profile_proc.wait()

    sv_proc = Popen([sys.executable, "-m", "snakeviz", "stats.prof"], shell=True)
    try:
        sleep(5)
        raise SystemExit
    except SystemExit:
        sv_proc.send_signal(signal.SIGTERM)

    sys.exit()
