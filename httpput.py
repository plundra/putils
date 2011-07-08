#!/usr/bin/env python
# Copyright (c) 2011, Pontus Lundkvist <plundra@lavabit.com>
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import urllib2
import sys

def httpput(url, data, headers={}):
    """
    Upload `data` to `url` via PUT-request
    Using optional `headers`
    """

    opener = urllib2.build_opener()
    request = urllib2.Request(url, data=data)
    
    # Add headers if given
    for header in headers:
        request.add_header(header, headers[header])
    
    # Replace get_method with something that returns PUT all the time
    request.get_method = lambda: 'PUT'
    
    # Execute the request
    result = opener.open(request)
    
    # Make sure we created the file
    if result.code != 201:
        raise IOError("%d: %s" % (result.code, result.msg))

def main():
    """Interactive usage example of httpput()"""
    if len(sys.argv) != 3:
        print "Usage: %s <file> <url>" % sys.argv[0]
        sys.exit(1)
    
    httpput(sys.argv[2], open(sys.argv[1]).read())

if __name__ == "__main__":
    main()
