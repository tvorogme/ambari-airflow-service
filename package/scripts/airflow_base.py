from resource_management import Execute, Script, File, Template, Directory
from resource_management.core.exceptions import ExecutionFailed
import os


class AirflowBase(Script):

    def install_airflow(self, env):
        import params
        env.set_params(params)

        Execute('yum groupinstall -y "Development Tools"')
        Execute("/opt/anaconda/bin/pip3 install 'pyqtwebengine<5.13' --force-reinstall")
        Execute('/opt/anaconda/bin/pip3 install "pyqt5<5.13" --force-reinstall')
        Execute('/opt/anaconda/bin/pip3 install apache-airflow==1.10.12 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.8.txt"')

        try:
            self.configure_airflow(env)
        except ExecutionFailed as ef:
            print("Error {0}".format(ef))
            return

    def configure_airflow(self, env):
        import params
        env.set_params(params)

        File("/etc/systemd/system/airflow_webserver.service",
             content=Template("webserver.j2",
                              configurations=params),
             owner='root',
             group='root',
             mode=0o0600
             )

        File("/etc/systemd/system/airflow_scheduler.service",
             content=Template("scheduler.j2",
                              configurations=params),
             owner='root',
             group='root',
             mode=0o0600
             )

    def install(self, env):
        self.install_airflow(self, env)
