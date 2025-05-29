import sys

if "--ignore" not in sys.argv and "-i" not in sys.argv:
    from subprocess import Popen
    from time import sleep
    import signal

    if "--fname" in sys.argv:
        try:
            output_file_name = sys.argv[sys.argv.index("--fname") + 1]
        except IndexError:
            raise RuntimeError("Unspecified filename")

    elif "-f" in sys.argv:
        try:
            output_file_name = sys.argv[sys.argv.index("-f") + 1]
        except IndexError:
            raise RuntimeError("Unspecified filename")

    else:
        output_file_name = "stats.prof"


    if "--gui" in sys.argv:
        try:
            gui_option = sys.argv[sys.argv.index("-gui") + 1]
        except IndexError:
            raise RuntimeError("Unspecified GUI option")

    elif "-g" in sys.argv:
        try:
            gui_option = sys.argv[sys.argv.index("--g") + 1]
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
            f"{sys.argv[0]}",
            "--ignore",
        ]
    )

    try:
        profile_proc.wait()

    except KeyboardInterrupt:
        pass

    sv_proc = Popen([sys.executable, "-m", gui_option, output_file_name])
    sleep(10)

    if sys.platform == "win32":
        sv_proc.send_signal(signal.CTRL_C_EVENT)
    else:
        sv_proc.send_signal(signal.SIGINT)

    sys.exit()