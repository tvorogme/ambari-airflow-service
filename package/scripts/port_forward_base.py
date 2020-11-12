from resource_management import Execute, Script, File, Template, Directory
from resource_management.core.exceptions import ExecutionFailed
import os


class PortForwardBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)
        self.configure_ac(env)

    def configure_ac(self, env):
        import params
        env.set_params(params)
        print("!!!!!!!!!!!!!!!!!!!!!!!creating file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        File("/etc/systemd/system/airflow_portforward.service",
             content=Template("portforward_service.j2", configurations=params),
             owner='root',
             group='root',
             mode=0o0600
             )
        Execute('sudo systemctl daemon-reload')

    def install(self, env):
        self.install_ac(env)
