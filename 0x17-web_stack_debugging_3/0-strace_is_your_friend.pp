# Fixing wordpress
exec { 'config':
path     => ['/usr/bin'],
cwd      => '/var/www/html/',
command  => '/bin/sed -i -e "s/.phpp/.php/g"  wp-settings.php',
provider => 'shell',
}