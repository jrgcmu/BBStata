# Description

These are Stata syntax highlighting modules for use with BBEdit and TextWrangler.

There are two versions:

1. `Stata.plist` is a minimal highlighting module that only uses Barebones' built-in text commands.

2. `Stata_RegEx.plist` uses regular expressions (generously contributed by Steve Samuels) to allow for recursive quotes (``"`string'"``) and both types of line comments (``\\`` and ``*``).

I have updated both of these with keywords from Stata 14.

**Note:** I am no longer updating the language module files, since [Jonathan  Marc Bearak's](http://bearak.org/code/text/index.html) language module also adds program definitions for code folding. (The only advantage of the more minimal version is that Bare Bones' built-in string functions seem a bit faster and more reliable than user-supplied regular expressions).

# Installation

Copy to 

```
~/Library/Application Support/BBEdit/Language Modules
```

replacing `BBEdit` with `TextWrangler` if you use the latter.


# Comment fill scripts

The scripts [CommentFill.scpt](https://github.com/jrgcmu/BBStata/blob/master/CommentFill.scpt) and [CommentFill.py](https://github.com/jrgcmu/BBStata/blob/master/CommentFill.py) add a space, followed by "*"s, to the end of the line (column 90 by default), which is useful for adding code-structuring comments (this is inspired by RStudio's version of this feature). The (vibe coded) Python script is the original version, but I added an AppleScript version since I realized Python is no longer installed by default. 

To install, put the Python script in the `Text filters` folder, or the AppleScript in the `Scripts` folder (from there, you can assign keyboard shortcuts).
