#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers and verifies deployment
"""

from fabric.api import put, run, env, local
from os.path import exists
env.hosts = ['100.27.227.145', '54.226.121.12']

def do_deploy(archive_path):
    """distributes an archive to the web servers and verifies deployment"""
    if not exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        check_deployment(no_ext)
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False

def check_deployment(no_ext):
    """Verifies if the deployment was successful by checking the HTTP status code of the deployed page"""
    for host in env.hosts:
        response = run('curl -o /dev/null -s -w "%{http_code}" http://{}:80/hbnb_static/0-index.html'.format(host))
        print(f"HTTP status for {host}: {response}")
        if response != '200':
            print(f"Deployment check failed on {host}")
        else:
            print(f"Deployment successful on {host}")
