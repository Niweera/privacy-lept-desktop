from os.path import abspath, join, dirname, realpath
import time
from PrivacyLeptHost import PrivacyLeptHost
from WindowsServiceBase import WindowsServiceBase
import logging


logging.basicConfig(
    filename=abspath(join(dirname(realpath(__file__)), "pld.log")),
    level=logging.INFO,
    format="[%(levelname).1s] [%(asctime)s] %(message)s [%(funcName)s]",
    datefmt="%d-%m-%Y %I:%M:%S %p",
)


class WindowsService(WindowsServiceBase):
    _svc_name_ = "privacy-lept-desktop"
    _svc_display_name_ = "Privacy-Lept Desktop Host"
    _svc_description_ = "Desktop host of Privacy-Lept system"

    def __init__(self, args):
        super().__init__(args)
        self.is_running = None

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def main(self):
        while self.is_running:
            PrivacyLeptHost.notify()
            time.sleep(10)


if __name__ == "__main__":
    logging.info("service installed")
    WindowsService.parse_command_line()
