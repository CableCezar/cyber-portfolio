#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python log_parse.py <file>")
        sys.exit(1)
    count = 0
    with open(sys.argv[1], 'r', errors='ignore') as f:
        for line in f:
            if 'error' in line.lower():
                count += 1
    print(f"Lines containing 'error': {count}")

if __name__ == "__main__":
    main()
