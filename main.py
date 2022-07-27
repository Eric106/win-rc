
from modules import ssh_util as SSH_U


server = SSH_U.sshTunnelManager(
    ssh_host='eserv.ddns.net',
    ssh_port=25522,
    ssh_user='tunel',
    ssh_key='C:/Users/eric/.ssh/eserv.ddns.net-tunel.pem',
    ssh_remote_forward='0.0.0.0:5900:10.169.0.9:5900'
)

try:
    while True:
        server.ssh_tunnel()
except:
    exit()