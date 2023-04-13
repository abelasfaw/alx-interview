#!/usr/bin/env python3
'''Log parsing'''
import sys
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_counter = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_counter = 0
total_size = 0


def print_metrics():
    '''prints calculated total size and status cod counts'''
    print("File size: {}".format(total_size))
    for k, v in code_counter.items():
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            line_counter += 1
            status_code = int(line.rstrip().split('\"')[2].split()[0])
            size = int(line.rstrip().split('\"')[2].split()[1])
            if (status_code in status_codes):
                total_size += size
                code_counter[str(status_code)] += 1
            if (line_counter == 10):
                print_metrics()
                line_counter = 0
    except KeyboardInterrupt:
        print_metrics()
        sys.stderr.flush()
        traceback.print_exc()
