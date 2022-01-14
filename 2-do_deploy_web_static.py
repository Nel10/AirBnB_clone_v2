#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone
"""
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ["35.231.214.154", "18.232.149.70"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        ext_not = file_name.split(".")[0]
        rout_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(rout_path, ext_not))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, rout_path, ext_not))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(rout_path, ext_not))
        run('rm -rf {}{}/web_static'.format(rout_path, ext_not))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(rout_path, ext_not))
        return True
    except Exception:
        return False
