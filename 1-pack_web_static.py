#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date
import os

def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    local("sudo mkdir -p versions")

    file_name = strftime("%Y%m%d%H%M%S")

    local("sudo tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_name))
    file_path = f"versions/web_static_{file_name}.tgz"
    file_size = os.path.getsize(file_path)
    print(f"web_static packed: {file_path}.tgz -> {file_size}Bytes")

#  return "versions/web_static_{}.tgz".format(filename)
