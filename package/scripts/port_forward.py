from resource_management import *
from port_forward_base import PortForwardBase
from resource_management.core.exceptions import ExecutionFailed, ComponentIsNotRunning
import subprocess

class JupyterServer(PortForwardBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)
        print("Installing Port forwarding")

    def configure(self, env):
        import params
        env.set_params(params)
        self.configure_ac(env)
        reload_cmd = format("systemctl reload airflow_portforward")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting portforward")
        start_cmd = format("systemctl start airflow_portforward")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping portforward")
        stop_cmd = format("systemctl stop airflow_portforward")
        Execute(stop_cmd)

    def restart(self, env):
        self.configure_ac(env)
        print("Restartarting port forwarding")
        Execute('systemctl restart airflow_portforward')

    def status(self, env):
        print("Checking portforward status...")

        try:
            Execute('systemctl status airflow_portforward')
        except ExecutionFailed:
            raise ComponentIsNotRunning

if __name__ == "__main__":
    JupyterServer().execute()
