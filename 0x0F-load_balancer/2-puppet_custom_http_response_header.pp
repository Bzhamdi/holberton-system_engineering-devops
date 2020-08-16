#!/usr/bin/env bash
# ngnix configuration  with puppet

exec {'header':
command  => 'file=$(cat /etc/nginx/sites-enabled/default); sudo apt-get -y update && 
             sudo apt-get -y install nginx && 
             sudo sed -i "40i \\\tadd_header X-Served-By \$hostname;\n" $file &&
             sudo service nginx restart',
provider => shell,
}
