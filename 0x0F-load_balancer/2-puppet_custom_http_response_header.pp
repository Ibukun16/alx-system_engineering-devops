# Creating atom HTTP header with Puppet

exec {'update':
  provider => shell,
  command  => '/usr/bin/sudo apt-get -y pdate',
  before   => Exec['install Nginx'],
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://github.com/Ibukun16 permanent;',
  require => Package['nginx'],
}

file_line { 'addHeader':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'run':
  provider => shell,
  command  => 'sudo service nginx restart'
  require  => Package['nginx'],
}
