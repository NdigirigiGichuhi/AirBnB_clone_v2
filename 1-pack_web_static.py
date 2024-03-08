#!/usr/bin/python3
"""A module for fabric script that generates .tzg archive"""
from fabric.api import local
from time import strftime
from datetime import date
import os


def do_pack():
    """ A script that generates archive the contents of web_static folder"""
    file_name = strftime("%Y%m%d%H%M%S")

    try:
        # Create a versions directory if it doesn't exist
        local("sudo mkdir -p versions")

        # Formatting the time stamp
        file_name = strftime("%Y%m%d%H%M%S")

        # Compressing the web_static folder into .tgz archive
        local(f"sudo tar -czvf versions/web_static_{file_name}.tgz \
                web_static/")

        # Defining the archive name
        file_path = f"versions/web_static_{file_name}.tgz"

        # Getting the file size
        file_size = os.path.getsize(file_path)
        print(f"web_static packed: {file_path}.tgz -> {file_size}Bytes")

        # Returning the archive path
        return "versions/web_static_{}.tgz".format(file_name)
    except Exception as e:
        return none
