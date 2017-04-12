from fabric.api import *

env.use_ssh_config = True

def production():
  env.hosts = ['172.31.9.12']


def deploy():
  run('whoami')


