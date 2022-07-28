from os import getenv
from time import sleep
from modules import ssh_util as SSH_U


user_folder = getenv('USERPROFILE').replace('\\','/')
server = SSH_U.sshTunnelManager(
    ssh_host='eserv.ddns.net',
    ssh_port=25522,
    ssh_user='tunel',
    ssh_key=user_folder+'/.ssh/eserv.ddns.net-tunel.pem',
)

try:
    t_name = server.new_tunel_forward(
        '0.0.0.0:5900:192.168.0.175:5900',
        SSH_U.sshForwardType.REMOTE
    )
    print(t_name)
    sleep(20)
    server.ssh_tunnels[t_name].stop()
except KeyboardInterrupt:
    exit()