from sys import argv

if "--ignore" not in argv:
    from subprocess import Popen
    from time import sleep
    import sys
    import signal

    if "--fname" in argv:
        try:
            output_file_name = argv[argv.index("--fname") + 1]
        except IndexError:
            raise RuntimeError("Unspecified filename")
    
    else:
	output_file_name = "stats.prof"

    if "--gui" in argv:
        try:
            gui_option = argv[argv.index("--gui") + 1]
        except IndexError:
            raise RuntimeError("Unspecified GUI option")

    else:
	gui_option = 'snakeviz'

    profile_proc = Popen(
        [
            f"{sys.executable}",
            "-m",
            "cProfile",
            "-o",
            output_file_name,
            f"{argv[0]}",
            "--ignore",
        ]
    )
    try:
        profile_proc.wait()

    except KeyboardInterrupt:
        pass

    sv_proc = Popen([sys.executable, "-m", gui_option, output_file_name])
    sleep(10)
    sv_proc.send_signal(signal.SIGINT)

    sys.exit()
