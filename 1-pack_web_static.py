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
        local("sudo mkdir -p versions")

        file_name = strftime("%Y%m%d%H%M%S")

        local(f"sudo tar -czvf versions/web_static_{file_name}.tgz web_static/")
        file_path = f"versions/web_static_{file_name}.tgz"
        file_size = os.path.getsize(file_path)
        print(f"web_static packed: {file_path}.tgz -> {file_size}Bytes")

        return "versions/web_static_{}.tgz".format(file_name)
    except Exception as e:
        return none
