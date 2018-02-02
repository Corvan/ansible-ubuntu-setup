#!/usr/bin/python3.6
import fileinput

for line in fileinput.input():
    line = line.rstrip()
    print("- name: Installing {}".format(line))
    print("  apt: name={} state=present")
    print("  tags: Auto")
    print("")
