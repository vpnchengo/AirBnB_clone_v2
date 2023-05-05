#!/usr/bin/python3
"""
a Fabric script generating .tgz archive from contents of web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local, env
import datetime


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
