#!/usr/bin/env python3
import os

base = os.path.expanduser(
    "~/Library/Containers/com.apple.mail/Data/Library/Mail Downloads")


def cleaner(base):
    for root, dirs, files in os.walk(base, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def main():
    cleaner(base)


if __name__ == '__main__':
    main()
