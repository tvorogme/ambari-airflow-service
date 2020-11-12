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
        Execute("service airflow_webserver reload")
        Execute("service airflow_scheduler reload")

    def start(self, env):
        print("Starting airflow")
        Execute("service airflow_webserver start")
        Execute("service airflow_scheduler start")

    def stop(self, env):
        print("Stopping airflow")
        Execute("service airflow_webserver stop")
        Execute("service airflow_scheduler stop")

    def restart(self, env):
        self.configure_airflow(env)
        print("Restartarting airflow")
        Execute("service airflow_webserver restart")
        Execute("service airflow_scheduler restart")

    def status(self, env):
        print("Checking airflow status...")
        Execute('service airflow_webserver status')
        Execute("service airflow_scheduler status")

if __name__ == "__main__":
    AirflowServer().execute()
