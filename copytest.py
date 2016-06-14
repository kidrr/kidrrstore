import sys
import os
import shutil
import xml.dom.minidom
try:
    from argparse import OptionParser
except:
    from optparse import OptionParser

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                shutil.copy2(s, d)

def main(argv):
    parser = OptionParser()
    parser.add_option("-s", "--src", dest="source",
                  help="source directory DIR", metavar="DIR")
    parser.add_option("-d", "--dst", dest="dest",
                  help="target directory DIR", metavar="DIR")
    

    (options, args) = parser.parse_args(argv)
    sourceDir = options.source
    targetDir = options.dest
    print sourceDir
    print targetDir
    copytree(sourceDir, targetDir)


if __name__ == '__main__':
    sys.exit(main(sys.argv))