A simple library for a one-liner performance profile using `cProfile`
and `snakeviz`! Upon import, will profile your code (profile file will
be `stats.prof` in your current working directory) and launch `snakeviz`
to visualize it. Snakeviz's webserver will be open for about 5 seconds
before it gets killed by `ez_profile`. The webpage will still be visible
and interactable though, until you refresh the page.

There is a current problem with IDLE where the webserver may not be killed,
but a `SystemError` will get raised. So, in the meantime I recommend not
using IDLE to run your code with `ez_profile` imported.

This is meant for internal usage, but if you don't want `ez_profile` to profile
your code, you can pass the `--ignore` commandline flag. This will bypass `ez_profile`
completely.

Usage:

```
import ez_profile # this is all you need

<all of your other code>
```

Credit for the idea goes to [matiiss](https://github.com/matiiss)
