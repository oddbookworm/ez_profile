import cProfile

profiler = cProfile.Profile()
profiler.enable()


def on_exit():
    profiler.disable()
    profiler.dump_stats("stats.prof")
