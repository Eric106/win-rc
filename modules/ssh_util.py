
from os import system
from os.path import abspath
from datetime import datetime
from enum import Enum
from threading import Thread
from dataclasses import dataclass, field


class sshForwardType(Enum):
    LOCAL = 'local'
    REMOTE = 'remote'


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


@dataclass(frozen=True)
class sshTunnelManager:
    ssh_user: str
    ssh_host: str
    ssh_port: int
    ssh_key: str
    ssh_bin : str = abspath('ssh/OpenSSH-Win64/ssh.exe')
    ssh_tunnels : dict = field(init=False)

    def __post_init__(self):
        object.__setattr__(self,"ssh_tunnels",dict())

    def __tunnel_forward(self, port_forward:str, forwardType: sshForwardType) -> int:
        if forwardType == sshForwardType.LOCAL:
            port_forward = f"-L {port_forward}"
        if forwardType == sshForwardType.REMOTE:
            port_forward = f"-R {port_forward}"
        # conn_str = f"{self.ssh_bin} -i {self.ssh_key} {port_forward} -vv -NT -p {self.ssh_port} {self.ssh_user}@{self.ssh_host}"
        conn_str = f"{self.ssh_bin} -i {self.ssh_key} {port_forward} -NT -p {self.ssh_port} {self.ssh_user}@{self.ssh_host}"
        print(conn_str)
        system(conn_str)
        return 1
        
    def __thread_tunnel_forward(self, port_forward:str, forwardType: sshForwardType) -> ThreadWithReturnValue:
        return ThreadWithReturnValue(
            target=self.__tunnel_forward,
            args=[port_forward, forwardType]
        )
    
    def new_tunel_forward(self,port_forward:str, forwardType: sshForwardType) -> str:
        thread_name = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
        self.ssh_tunnels[thread_name] = self.__thread_tunnel_forward(port_forward, forwardType)
        self.ssh_tunnels[thread_name].start()
        return thread_name


    