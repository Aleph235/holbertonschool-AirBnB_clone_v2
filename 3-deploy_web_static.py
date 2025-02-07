#!/usr/bin/python3
"""deploy everything to the web  servers"""

from fabric.api import run, put, env, local
import datetime
import os.path
env.hosts = ['54.144.49.141', '54.242.182.44i']


def deploy():
    """pack and deply folders"""
    file = do_pack()
    if file is None:
        return False
    deploy = do_deploy(file)
    return deploy


def do_pack():
    """pack folder"""
    try:
        date_format = "%Y%m%d%H%M%S"
        date = datetime.datetime.now().strftime(date_format)
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(name))
        size = os.path.getsize(name)
        print("web_static packed: {} -> {}Bytes".format(name, size))
        return name
    except ValueError:
        return None


def do_deploy(archive_path):
    """deploy archive"""
    if os.path.exists(archive_path):
        file = archive_path.split("/")[-1]
        rm = file.split(".")[0]
        path = "/data/web_static/releases/"
        path2 = "/data/web_static/current"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(path, rm))

        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, rm))

        run('rm /tmp/{}'.format(file))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, rm))

        run('rm -rf {}{}/web_static'.format(path, rm))

        run('rm -rf {}'.format(path2))

        run('ln -s {}{}/ {}'.format(path, rm, path2))

        print("New version deployed!")

        return True

    return False
