# Python-jsMinifier
Python code that minifies all js files in a directory and uploads them to device running Mongoose OS. This saves ~20k or more of file space, useful for ESP-01.

Code uses jsmin package https://pypi.python.org/pypi/jsmin

Note: Code will try to minify all files in dir, so only place .js files in dir. Code will attempt to "put" files onto device. Program will also fill up working directory with minified files since I had trouble with putting paths in the mos.exe put command.
