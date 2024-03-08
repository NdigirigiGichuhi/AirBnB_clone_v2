#!/usr/bin/python3
"""A Fabric Script that distributes archives on web servers"""

from fabric.api import env, run, put
from os import path
from datetime import datetime

env.hosts = ['18.215.160.180', '3.95.32.201']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Create a tar gzipped archive of the web_static directory"""
    # Obtaining current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    # Construct path where the archive is saved
    archive_path = "versions/web_static_{}.tgz".format(now)

    # Create a directory if it does not exist using fabric
    local("mkdir -p versions")

    # Use tar command to create and compress archive
    archived = local("tar -cvzf {} web_static".format(archive_path))

    # Checking archive status
    if archived.return_code != 0:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    """ Distributes an archive to each web server

    Arguments:
        archive_path (str): The path of the archive to distribute
    Returns:
        If file doesn't exist at path - False
        Otherwise - True
    """
    # Checking for valid path
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(
                file_name.split('.')[0])

        put(archive_path, '/tmp')

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
