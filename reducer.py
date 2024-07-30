#!/usr/bin/env python
import sys

def reducer():
    current_city = None
    current_count = 0
    city = None

    for line in sys.stdin:
        # Remove leading and trailing whitespace
        line = line.strip()
        # Parse the input from the mapper
        city, count = line.split('\t', 1)

        # Convert count (currently a string) to int
        try:
            count = int(count)
        except ValueError:
            continue

        if current_city == city:
            current_count += count
        else:
            if current_city:
                # Write result to stdout
                print '%s\t%s' % (current_city, current_count)
            current_count = count
            current_city = city

    if current_city == city:
        print '%s\t%s' % (current_city, current_count)

if __name__ == "__main__":
    reducer()
