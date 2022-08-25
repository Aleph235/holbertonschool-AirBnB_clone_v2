#!/usr/bin/python3
"""Deploy archive to your servers"""

import os.path
from fabric.api import run, put, env
env.hosts = ['54.144.49.141', '54.242.182.44']


def do_deploy(archive_path):
    """Deploy archived folder to the server"""
    if os.path.exists(archive_path):
        file = archive_path.split("/")[-1]
        rm = file.split(".")[0]
        path = "/data/web_static/releases/"
        path_1 = "/data/web_static/current"

        put(archive_path, '/tmp/')

        run('mkdir -p {}{}/'.format(path, rm))

        run('tar -xzf /tmp/{} -C {}{}/'.format(file, path, rm))

        run('rm /tmp/{}'.format(file))

        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, rm))

        run('rm -rf {}{}/web_static'.format(path, rm))

        run('rm -rf {}'.format(path_1))

        run('ln -s {}{}/ {}'.format(path, rm, path_1))

        print("New version deployed!")

        return True

    return False
