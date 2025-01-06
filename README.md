# nessus-monitoring
a python script to send notification from nessus server to telegram.

## Set up service
Please make sure the service file is in the right PATH --> /etc/systemd/system/resource_monitor.service

bash```
// enable the service
$ sudo systemctl enable resource_monitor

// start the service
$ sudo systemctl start resource_monitor
```
