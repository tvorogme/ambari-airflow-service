from resource_management import *
from airflow_base import AirflowBase
from resource_management.core.exceptions import ExecutionFailed
import subprocess

class AirflowServer(AirflowBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_airflow(env)
        print("Installing Airflow")

    def configure(self, env):
        import params
        env.set_params(params)
        self.configure_airflow(env)
        Execute("service webserver reload")
        Execute("service scheduler reload")

    def start(self, env):
        print("Starting airflow")
        Execute("service webserver start")
        Execute("service scheduler start")

    def stop(self, env):
        print("Stopping airflow")
        Execute("service webserver stop")
        Execute("service scheduler stop")

    def restart(self, env):
        self.configure_airflow(env)
        print("Restartarting airflow")
        Execute("service webserver restart")
        Execute("service scheduler restart")

    def status(self, env):
        print("Checking airflow status...")
        Execute('service webserver status')
        Execute("service scheduler status")

if __name__ == "__main__":
    JupyterServer().execute()
