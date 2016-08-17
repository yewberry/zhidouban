#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import src.my_glob as my_glob

try:
    import src as mysrc
    IS_LOCAL = True
except ImportError:
    try:
        import ZhiDouBan as mysrc
        IS_LOCAL = False
    except ImportError, msg:
        print "There was an error while tring to import ZhiDouBan"
        print "ERROR MSG: "
        print str(msg)
        os._exit(1)


def main():
    # Set src path to sys.path.
    SRC_DIR = os.path.dirname(mysrc.__file__)
    if not IS_LOCAL:
        SRC_DIR = os.path.join(SRC_DIR, 'src')

    # Cleanup any modules that are already present before importing
    if not IS_LOCAL:
        torem = [key for key in sys.modules.keys() if key.startswith('yew')]
        for key in torem:
            del sys.modules[key]
    else:
        if 'src' in sys.modules:
            del sys.modules['src']

    sys.path.insert(0, SRC_DIR)
    from src.ZhiDouBan import ZhiDouBan
    app = ZhiDouBan()
    app.start()

if __name__ == '__main__':
    main()

