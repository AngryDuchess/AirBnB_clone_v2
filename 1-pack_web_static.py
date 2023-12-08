#!/usr/bin/python3
""" do pack function"""

from fabric.api import local
from datetime import datetime as time


def do_pack():
    """function do pack """
    try:
        time_stamp = time.now().strftime("%Y%m%d%H%M%S")
        saved_path = "versions/web_static_{}.tgz".format(
            time_stamp
        )
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(
            saved_path
        ))
    except Exception:
        return None
    else:
        return saved_path
