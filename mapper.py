#!/usr/bin/env python
import sys

def mapper():
    for line in sys.stdin:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Split the line into columns based on comma
        data = line.split(",")
        if len(data) > 5:  # Ensure there are enough columns
            city = data[5]
            print '%s\t%s' % (city, 1)

if __name__ == "__main__":
    mapper()
