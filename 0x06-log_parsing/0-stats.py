#!/usr/bin/python3
"""
Module that parses a log and prints stats to stdout
"""
from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def print_stats():
    """Prints the accumulated logs"""
    print("File size: {}".format(size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                items = line.split()
                size += int(items[-1])
                if items[-2] in status_codes:
                    status_codes[items[-2]] += 1
            except:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()

'''

def checkInputLog(theInput):
    """ check if the format is the next or else return None
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code>
        <file size>
    """

    getIp = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\-\s"
    getDate = "\[\d{4}\-\d{2}\-\d{2}\s\d{2}\:\d{2}\:\d{2}\.\d{6}\]\s"
    getRequest = "\"GET \/projects\/260 HTTP\/1.1\"\s"
    getStatus_File = "\d{3}\s\d{1,4}$"
    pattern = getIp + getDate + getRequest + getStatus_File
    return re.match(pattern, theInput)


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats(status_codes, size):
    """Prints the accumulated logs"""
    print("File size: {}".format(size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))


size = 0

if __name__ == "__main__":
    dicCodes = 0
    countLine = 0
    try:
        for line in sys.stdin:
            try:
                countLine += 1
                getLogs = line.split()
                size += int(getLogs[-1])
                if (checkInputLog(line) is not None and getLogs[-2] in
                        status_codes):
                    status_codes[getLogs[-2]] += 1

                if countLine % 10 == 0:
                    print_stats(status_codes, size)
            except:
                pass
    except KeyboardInterrupt:
        print_stats(status_codes, size)
        raise
    print_stats(status_codes, size)
'''
