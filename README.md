# Description

These are Stata syntax highlighting modules for use with BBEdit and TextWrangler.

There are two versions:

1. `Stata.plist` is a minimal highlighting module that only uses Barebones' built-in text commands.

2. `Stata_RegEx.plist` uses regular expressions (generously contributed by Steve Samuels) to allow for recursive quotes (``"`string'"``) and both types of line comments (``\\`` and ``*``).

I have updated both of these with keywords from Stata 14.

You may also be interested in [Jonathan  Marc Bearak's](http://bearak.org/code/text/index.html) version, which also adds program definitions for code folding.

The only advantage of the more minimal version is that Bare Bones' built-in string functions seem a bit faster and more reliable than user-supplied regular expressions.


# Installation

Copy to 

```
~/Library/Application Support/BBEdit/Language Modules
```

replacing `BBEdit` with `TextWrangler` if you use the latter.
