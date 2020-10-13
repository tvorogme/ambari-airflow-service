from resource_management import Execute, Script
from resource_management.core.exceptions import ExecutionFailed


class AnacondaBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)

        try:
            Execute("cd /tmp")
            Execute("curl -O https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh")
            Execute("bash Anaconda3-2020.07-Linux-x86_64.sh -b -p /opt/anaconda")
        except ExecutionFailed as ef:
            print(f"Error, maybe installed {ef}")

        filestr = """[Unit]
Description=ROT13 demo service
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=centos
ExecStart=/usr/bin/env php /path/to/server.php

[Install]
WantedBy=multi-user.target"""
        Execute(f'echo "{filestr}" > /etc/systemd/system/jupyter.service')

    def install(self, env):
        self.install_ac(self, env)
