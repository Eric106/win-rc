import platform
from subprocess import Popen
from os.path import abspath
from datetime import datetime
from enum import Enum
from threading import Thread, Event, current_thread
from dataclasses import dataclass, field


class sshForwardType(Enum):
    LOCAL = '-L'
    REMOTE = '-R'


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
        self._stop = Event()
    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def stopped(self):
        return self._stop.isSet()
    def stop(self):
        self._stop.set()
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


@dataclass(frozen=True)
class sshTunnelManager:
    ssh_user: str
    ssh_host: str
    ssh_port: int
    ssh_key: str
    ssh_bin : str = field(init=False)
    ssh_tunnels : dict = field(init=False)

    def __post_init__(self):
        object.__setattr__(self,"ssh_bin",
            abspath('bin/ssh/OpenSSH-Win64/ssh.exe') if platform.system() == 'Windows' else '/usr/bin/ssh'
        )
        object.__setattr__(self,"ssh_tunnels",dict())

    def __tunnel_forward(self, port_forward:str, forwardType: sshForwardType):
        port_forward = f"{forwardType.value} {port_forward}"
        ssh_command = [self.ssh_bin,
                    '-i', self.ssh_key, port_forward,
                    '-NT' ,'-p', str(self.ssh_port),
                    '-o', 'StrictHostKeyChecking=no',
                    f'{self.ssh_user}@{self.ssh_host}']
        print(" ".join(ssh_command))
        ssh_command = Popen(ssh_command)
        while True:
            if current_thread().stopped():
                ssh_command.kill()
                break               
        
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


    