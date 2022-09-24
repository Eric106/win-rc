import sys
from os import system
from time import sleep
from modules import ssh_util as SSH_U
from modules import ip_util as IPU



default_ip = IPU.get_default_ip()
server = SSH_U.sshTunnelManager(
    ssh_host='eserv.ddns.net',
    ssh_port=25522,
    ssh_user='tunel',
    ssh_key='keys/eserv.ddns.net-tunel.pem',
)

t_name : str = ''
try:
    t_name = server.new_tunel_forward(
        f'0.0.0.0:5900:{default_ip}:5900',
        SSH_U.sshForwardType.REMOTE)
    while True:
        system(f'netstat -np TCP | find "{server.ssh_port}"')
        sleep(5)
except KeyboardInterrupt:
    server.ssh_tunnels[t_name].stop()
    sys.exit()
