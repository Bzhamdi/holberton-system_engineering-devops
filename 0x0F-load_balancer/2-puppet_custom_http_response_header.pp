#!/usr/bin/env bash
# ngnix configuration  with puppet

exec {'header':
command  => 'hostname=$(cat /etc/hostname) &&
	     sudo apt-get -y update && 
             sudo apt-get -y install nginx && 
             sudo sed -i "40i \\\tadd_header X-Served-By \$hostname;\n" /etc/nginx/sites-enabled/default &&
             sudo service nginx restart',
provider => shell,
}
