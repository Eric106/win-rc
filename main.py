
from modules import ssh_util as SSH_U


server = SSH_U.sshTunnelManager(
    ssh_host='eserv.ddns.net',
    ssh_port=25522,
    ssh_user='tunel',
    ssh_key='C:/Users/eric/.ssh/eserv.ddns.net-tunel.pem',
)

try:
    t_name = server.new_tunel_forward(
        '0.0.0.0:3390:10.169.0.9:3389',
        SSH_U.sshForwardType.REMOTE
    )
    print(t_name)
except KeyboardInterrupt:
    exit()