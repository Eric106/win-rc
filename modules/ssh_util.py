from threading import Thread
from os import system
from dataclasses import dataclass, field


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
    ssh_remote_forward: str = field(default=None)
    ssh_local_forward: str = field(default=None)
    ssh_bin : str = "ssh/OpenSSH-Win64/ssh.exe"
    ssh_tunnels : dict = field(init=False)

    def __post_init__(self):
        object.__setattr__(self,"ssh_tunels",dict())
    
    def ssh_tunnel(self):
        connection_ssh = str()
        port_forward = str()
        if self.ssh_local_forward != None and self.ssh_remote_forward == None:
            port_forward = port_forward + f"-L {self.ssh_local_forward}"
        if self.ssh_local_forward == None and self.ssh_remote_forward != None:
            port_forward = port_forward + f"-R {self.ssh_remote_forward}"  

        connection_ssh = f"{self.ssh_bin} -i {self.ssh_key} {port_forward} -vv -NT -p {self.ssh_port} {self.ssh_user}@{self.ssh_host}"
        print(connection_ssh)
        system(connection_ssh)
        
