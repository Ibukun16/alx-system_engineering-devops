# Script that modify nginx setting to handle more requests

exec {'modify-max limit setting file':
  command => 'sudo sed -i "s/15/10000/g" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  provider => 'shell',
}
