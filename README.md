A simple library for a one-liner performance profile using `cProfile`
and `snakeviz`! Upon import, will profile your code (profile file will
be `stats.prof` in your current working directory) and launch `snakeviz`
to visualize it. The snakeviz webserver will be open for about 5 seconds
before it gets killed by `ez_profile`. The webpage will still be visible
and interactable though, until you refresh the page.

There is a current problem with IDLE where the webserver may not be killed,
but a `SystemError` will get raised. So, in the meantime I recommend not
using IDLE to run your code with `ez_profile` imported.

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

Credit for the idea goes to [matiiss](https://github.com/matiiss)
