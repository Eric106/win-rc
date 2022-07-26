# WIN-RC 

## RC-Server config

### Redirect VNC to RC-Server over SSH
```shell
ssh -R 0.0.0.0:5900:HOSTIP:5900 -vv -N -p 25522 user@rc-server-ip
```

### Edit RC-Server to admit Gateway setting
Edit on file `/etc/ssh/sshd_config`
```/etc/ssh/sshd_config
GatewayPorts clientspecified
```

### Edit RC-Server to change SSH port and keepAlive
Edit on file `/etc/ssh/sshd_config`
```/etc/ssh/sshd_config
Port 25522
...
ClientAliveInterval 60
ClientAliveCountMax 2
```

### Edit RC-Server to set SSH key auth

Create SSH key pairs (OPTIONAL if you dont have any keys)
```shell
ssh-keygen -t rsa -b 2048
```

At RC-server on each `.ssh` user folder set the pub key.
```shell
ssh-copy-id -p PORTNUMBER user@rc-server-hostname
```

Retrive private key to be used on SSH connections (EXAMPLE: `ssh -i priv_key.pem user@rc-server-ip`)
```shell
sudo cat /home/user/.ssh/id_rsa >> rc-server.pem
```

Edit on file `/etc/ssh/sshd_config`
```/etc/ssh/sshd_config
PubkeyAuthentication yes

# Expect .ssh/authorized_keys2 to be disregarded by default in future.
AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2
...
PasswordAuthentication no
```
