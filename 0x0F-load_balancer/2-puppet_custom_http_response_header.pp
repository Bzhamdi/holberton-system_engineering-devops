#!/usr/bin/env bash
# ngnix configuration  with puppet
node {'nginx':
	$myvar = $file="/etc/nginx/sites-enabled/default",
}
exec {'http_header':
command  => 'sudo apt-get -y update && 
             sudo apt-get -y install nginx && 
             sudo sed -i "30i \\\tadd_header X-Served-By \$hostname;\n" $file  &&
             sudo service nginx restart',
provider => shell,
}
