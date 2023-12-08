#!/usr/bin/python3
""" a function"""

from fabric.api import local, run, env, put
from datetime import datetime as time
from os import path


env.hosts = ["18.207.233.37"]


def do_pack():
    """ do pack function """
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


def do_deploy(archive_path):
    """ do deploy function"""
    try:
        if not path.exists(archive_path):
            return False

        releases = "/data/web_static/releases/"
        web_static_dir = path.basename(archive_path).split(".")[0]

        put(local_path=archive_path, remote_path="/tmp/")

        run("mkdir -p {}/{}".format(
            releases,
            web_static_dir
        ))
        run("tar -xzf /tmp/{} -C {}/{}".format(
            archive_path,
            releases,
            web_static_dir
        ))

        run("rm -f /tmp/{}".format(
            archive_path
        ))

        run("mv {0}/{1}/web_static/* {0}/{1}".format(
            releases,
            web_static_dir,
        ))

        run("rm -rf {}/{}/web_static".format(
            releases, web_static_dir
        ))

        run("rm -rf /data/web_static/current")

        run("ln -s {}/{}/ /data/web_static/current".format(
            releases, web_static_dir
        ))

        print("New version deployed!")
        return True

    except Exception:
        return False
