A simple library for a one-liner performance profile using `cProfile`
and `snakeviz`! Upon import, will profile your code (profile file will
be `stats.prof` in your current working directory) and launch `snakeviz`
to visualize it. Snakeviz's webserver will be open for about 5 seconds
before it gets killed by `ez_profile`. The webpage will still be visible
and interactable though, until you refresh the page.

Usage:

```
import ez_profile # this is all you need

<all of your other code>
```

Credit for the idea goes to [matiiss](https://github.com/matiiss)
