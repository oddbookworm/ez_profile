Releases can be installed via pip from [pypi](https://pypi.org/project/ez-profile/)

A simple library for a one-liner performance profile using `cProfile`
and `snakeviz`! Upon import, will profile your code (profile file will
be `stats.prof` in your current working directory) and launch `snakeviz`
to visualize it. The snakeviz webserver will be open for about 5 seconds
before it gets killed by `ez_profile`. The webpage will still be visible
and interactable though, until you refresh the page.

There is a problem with IDLE where the webserver may not be killed,
but a `SystemError` will get raised. This is a known problem and appears to
be an issue with IDLE and/or Python itself. If I find a solution, I will
fix the problem, but for now IDLE is considered incompatible with `ez_profile`.

This is meant for internal usage, but if you dont want `ez_profile` to profile
your code, you can pass the `--ignore` commandline flag. This will bypass `ez_profile`
completely.

Notes about usage:
`import ez_profile` should be at the top of your main file. It profiles the
entire project, and to do so, it runs the main file in a separate process.
If you put this anywhere else in your project, the part before `import ez_profile`
will not be profiled, and the whole project will be killed after the profiling is
completed.

Usage:

```
# note that this should be at the top of your script
import ez_profile # this is all you need

<all of your other code>
```

**New in 0.1.6**
`--fname` commandline argument to specify where you want the output profile to be saved
```
python file.py --fname "/path/to/custom/location/file.prof"
python file.py --fname "custom_filename.prof"
```

Credit for the idea goes to [matiiss](https://github.com/matiiss)
