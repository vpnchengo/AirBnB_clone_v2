#!/usr/bin/python3
"""
a Fabric script generating .tgz archive from contents of web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, env, put, run
import datetime
import os

env.user = 'ubuntu'
env.hosts = ['100.26.222.47', '35.153.67.249']


def do_pack():
    """
    generating .tgz archive from web_static folder
    """
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/{}/'.format(archive.split('.')[0])
        current = '/data/web_static/current'
        path_a = '/tmp/{}'.format(archive)
        put(archive_path, path_a)
        run('mkdir -p {}/'.format(path))
        run('tar -xzf {} -C {}'.format(path_a, path))
        run('rm {}'.format(path_a))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    return False
