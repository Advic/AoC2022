# Creates a new daily challenge module the way I like it set up
from os import walk, mkdir
from os.path import join

TEMPLATE_DIR = 'template'
DAY_PREFIX = 'Day'
DAY_REPL = 'DAYNUM'

daynum = str(int(input("Which AOC day is it? ")))
destdir = DAY_PREFIX + daynum

mkdir(destdir)
for (dirpath, dirnames, filenames) in walk(TEMPLATE_DIR):
    for filename in filenames:
        with open(join(dirpath, filename)) as source, \
                open(join(destdir, filename.replace(DAY_REPL, daynum)), 'w') as dest:
            dest.write(source.read().replace(DAY_REPL, daynum))
