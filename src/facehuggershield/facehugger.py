from nullscream import install_nullscream, uninstall_nullscream
import darklock


class Facehugger:
    def __init__(
        self,
        blacklist: list = None,
        whitelist: list = None,
        restrict_os_access: bool = False,
        no_internet_socket: bool = False,
    ):
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.restrict_os_access = restrict_os_access
        self.no_internet_socket = no_internet_socket

        if blacklist or whitelist:
            self.install_nullscream()

    def install_nullscream(self, blacklist=None, whitelist=None):
        install_nullscream(
            blacklist=self.blacklist,
            whitelist=self.whitelist
        )

    def uninstall_nullscream(self, blacklist=None, whitelist=None):
        uninstall_nullscream(
            blacklist=[],
            whitelist=[]
        )

    def lock_network(self):
        darklock.network.activate()

    def unlock_network(self):
        darklock.network.deactivate()
