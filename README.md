# Description

These are Stata syntax highlighting modules for use with BBEdit and TextWrangler.

There are two versions:

1. `Stata.plist` is a minimal highlighting module that only uses Barebones' built-in text commands.

2. `Stata_RegEx.plist` adds syntax highlighting for both the `\\` and `*` line comments using regular expressions generously contributed by Steve Samuels.

You may also be interested in [Jonathan  Marc Bearak's](http://bearak.org/code/text/index.html) version, which uses regular expressions to include multiple line comment types, program definitions (for code folding) and recursive string highlighting.


I prefer the first, more minimal module, because Bare Bones' built-in string pattern functions seem to be faster and more reliable. The disadvantages are that you have to choose which type of line comment you prefer (the default is `\\`).


# Installation

Copy to 

```
~/Library/Application Support/BBEdit/Language Modules
```

replacing `BBEdit` with `TextWrangler` if you use the latter.
