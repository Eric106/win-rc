# win-rc


## Redirect VNC to RC-Server over SSH
```shell
ssh -R 0.0.0.0:5900:HOSTIP:5900 -vv -N user@rc-server-ip
```

## Edit RC-Server to admit Gatway setting
Edit on file `/etc/ssh/sshd_config`
```shell
GatewayPorts clientspecified
```
