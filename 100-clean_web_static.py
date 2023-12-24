#!/usr/bin/python3
""" a function"""

from fabric.api import local, run, env, put, runs_once, lcd, cd
from datetime import datetime as time
from os import path, listdir


env.hosts = ["ubuntu@54.161.255.250", "ubuntu@54.236.33.119"]


@runs_once
def do_pack():
    """do pack function """
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

        releases = "/data/web_static/releases"
        web_static_dir = path.basename(archive_path).split(".")[0]

        put(local_path=archive_path, remote_path="/tmp/")

        run("rm -rf {}/{}".format(
            releases,
            web_static_dir
        ))

        run("mkdir -p {}/{}".format(
            releases,
            web_static_dir
        ))
        run("tar -xzf /tmp/{}.tgz -C {}/{}".format(
            web_static_dir,
            releases,
            web_static_dir
        ))

        run("rm -f /tmp/{}.tgz".format(
            web_static_dir
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


def deploy():
    """deploy function"""
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    """do clean function"""
    files = listdir("./versions")
    files = sorted(files)[::-1]

    number = 1 if number == 0 else number
    number = int(number)

    with lcd("versions"):
        for file in files[number:]:
            local("rm {}".format(file))

    with cd("/data/web_static/releases"):
        remote_files = run("ls")
        # print(remote_files.split()[::-1])
        filtered_files = [file for file in remote_files.split() if
                          "web_static_" in file]
        for file in filtered_files[number:]:
            run("rm -r {}".format(file))