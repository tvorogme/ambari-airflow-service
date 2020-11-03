from resource_management import *
from anaconda_base import AnacondaBase
from resource_management.core.exceptions import ExecutionFailed
import subprocess

class JupyterServer(AnacondaBase):

    def install(self, env):
        import params
        env.set_params(params)
        self.install_ac(env)
        print("Installing Ancaonda")

    def configure(self, env):
        import params
        env.set_params(params)
        self.configure_ac(env)
        reload_cmd = format("service jupyter reload")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting jupyter")
        start_cmd = format("service jupyter start")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping jupyter")
        stop_cmd = format("service jupyter stop")
        Execute(stop_cmd)

    def restart(self, env):
        self.configure_ac(env)
        print("Restartarting jupyter")
        Execute('service jupyter restart')

    def status(self, env):
        print("Checking jupyter status...")
        Execute('service jupyter status')

if __name__ == "__main__":
    JupyterServer().execute()
