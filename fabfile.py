from fabric.api import *

env.hosts = ['rama.icmconsulting.com']
env.shell = 'bash -c'

def deploy():
    sudo("cd /usr/home/img/img; git pull origin master ; chown -R img:img . ; ./manage.py collectstatic --noinput ; touch img.wsgi")

def getdb():
    run('pg_dump -U img img > /tmp/img.sql')
    get('/tmp/img.sql', '/tmp/img.sql')
    run('rm /tmp/img.sql')

def updatedb():
#    local('createuser -U postgres parsiena')
    local('dropdb -U img img')
    local('createdb -U img img')
    local('psql -U img img < /tmp/img.sql')
    local('rm /tmp/img.sql')

def syncdb():
    getdb()
    updatedb()
