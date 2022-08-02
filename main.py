import sys
from os import getenv, system
from time import sleep
from modules import ssh_util as SSH_U


user_folder = getenv('USERPROFILE').replace('\\','/')
server = SSH_U.sshTunnelManager(
    ssh_host='192.168.0.171',
    ssh_port=25522,
    ssh_user='tunel',
    ssh_key=user_folder+'/.ssh/eserv.ddns.net-tunel.pem',
)

try:
    t_name = server.new_tunel_forward(
        '0.0.0.0:5900:192.168.0.175:5900',
        SSH_U.sshForwardType.REMOTE)
    while True:
        system(f'netstat -np TCP | find "{server.ssh_port}"')
        sleep(5)
except KeyboardInterrupt:
    server.ssh_tunnels[t_name].stop()
    sys.exit()
