# PyDar
Python powered wifi radar

## v1. Requirements
Apache `sudo apt-get install apache2`
PHP `sudo apt-get install php` 

Visudo entry 
```
www-data ALL=(ALL) NOPASSWD:/usr/bin/pinout
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_left.py
www-data ALL=(ALL) NOPASSWD:/home/pi/PyDar/move_right.py
www-data ALL=(ALL) NOPASSWD:/usr/bin/python3
```

Ownership issues

`chown www-data:www-data /PyDar`

`chown www-data:www-data /var/www/html`

Remember to copy index.php to /var/www/html
## Docker GPIO access
`$ docker run --privileged -d whatever`

## TODO

* v1. Run on LAMP server on bare metal - DONE
* v2. Dockerize the app, change base docker image to `raspbian/stretch` use configs from https://github.com/joaquindlz/rpi-docker-lamp/blob/master/Dockerfile
* v3. Allow distributed containers on different systems to call the necessary functions


## Troubleshooting

Sometimes numpy will give you an error that it can't be imported even though you have already installed it through pip. If that happens try running `sudo apt-get install libatlas-base-dev`

## NodeJS Experimental Branch

Following some tutorial from https://medium.com/swlh/run-python-script-from-node-js-and-send-data-to-browser-15677fcf199f

To try and figure out this rendering nonsense. 

