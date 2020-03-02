#!/usr/bin/env python3
# Similar to Linux time utility for the Windows Command Prompt
import subprocess
import sys
import time

def main():
    command = ' '.join(sys.argv[1:])

    start = time.monotonic()
    subprocess.run(command, shell=True)
    end = time.monotonic()

    print('Elapsed Time: %.1f sec' % (end - start))

if __name__ == "__main__":
    main()