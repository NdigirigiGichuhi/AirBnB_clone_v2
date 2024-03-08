#!/usr/bin/python3
"""A Fabric Script that distributes archives on web servers"""

from fabric.api import env, run, put
from os import path

env.hosts = ['18.215.160.180', '3.95.32.201']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Distributes an archive to each web server

    Arguments:
        archive_path (str): The path of the archive to distribute
    Returns:
        If file doesn't exist at path - False
        Otherwise - True
    """
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp')

        # Uncompress archive to the folder
        file_name = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(
            file_name.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, release_folder))

        # Delete the archive from web server
        run('rm /tmp/{}'.format(file_name))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print('New version deployed!')
        return True
    except Exception as e:
        print('Error:', e)
        return False
