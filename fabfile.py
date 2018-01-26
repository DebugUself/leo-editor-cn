from fabric.api import *
import fabric.contrib.project as project
import os

env.input_path = 'docs'

env.deploy_path = 'html'

def build():
	local('cd {input_path} && make html'.format(**env))

def serve():
	local('cd {deploy_path} && python3 -m http.server 8000'.format(**env))

def reserve():
    build()
    serve()

def pub():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            'git add --all . && '
            'git commit -am "updaeing by local. " && '
            'git push && '
            'pwd '.format(**env)
)