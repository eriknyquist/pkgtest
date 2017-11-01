# Extract the contents of a Wheel (.whl) file and copy
# to a specific directory

import sys
import os
import argparse
import zipfile

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="Install a <> module")

parser.add_argument(dest="package_file", help="Package .whl file to install")

parser.add_argument("-d", "--directory", dest="install_dir",
    help="module installation directory (default is current directory)")

args = parser.parse_args()

def die(msg, err=1):
    print "Error: %s. Aborting" % msg
    sys.exit(err)

def main():
    dir_name, ext = os.path.splitext(args.package_file)

    if args.install_dir:
        dir_name = os.path.join(args.install_dir, dir_name)

    if ext != ".whl":
        die("package file %s does not end in '.whl'" % args.package_file)

    if dir_name.strip() == '':
        die("package file name %s has invalid format" % args.package_file)

    if os.path.isdir(dir_name):
        die("package directory %s already exists" % dir_name)

    os.mkdir(dir_name)
    with zipfile.ZipFile(args.package_file, 'r') as zf:
        zf.extractall(dir_name)

    print "Module installed in %s" % dir_name

if __name__ == "__main__":
    main()
