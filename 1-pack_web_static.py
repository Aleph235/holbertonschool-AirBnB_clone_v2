#!/usr/bin/python3
"""Compress before sending"""

import fabric.api
import datetime
import os.path


def do_pack():
    """Compress folder into .tar"""
    try:
        date_format = "%Y%m%d%H%M%S"
        date = datetime.datetime.now().strftime(date_format)
        if os.path.isdir("versions") is False:
            fabric.api.local("mkdir versions")
        name = "versions/web_static_{}.tgz".format(date)
        fabric.api.local("tar -cvzf {} web_static".format(name))
        size = os.path.getsize(name)
        print("web_static packed: {} -> {}Bytes".format(name, size))
        return name
    except ValueError:
        return None
