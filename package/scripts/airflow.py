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
        Execute("systemctl reload airflow_webserver")
        Execute("systemctl reload  airflow_scheduler")

    def start(self, env):
        print("Starting airflow")
        Execute("systemctl start airflow_webserver")
        Execute("systemctl start airflow_scheduler")

    def stop(self, env):
        print("Stopping airflow")
        Execute("systemctl stop airflow_webserver")
        Execute("systemctl stop airflow_scheduler")

    def restart(self, env):
        self.configure_airflow(env)
        print("Restartarting airflow")
        Execute("systemctl restart airflow_webserver")
        Execute("systemctl restart airflow_scheduler")

    def status(self, env):
        print("Checking airflow status...")
        Execute('systemctl status airflow_webserver')
        Execute("systemctl status airflow_scheduler")

if __name__ == "__main__":
    AirflowServer().execute()
