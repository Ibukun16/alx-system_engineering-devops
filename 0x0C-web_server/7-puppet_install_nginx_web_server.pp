# Puppet manifest to automate the installation of nginx 

package { 'nginx':
  ensure => 'installed',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.jw.org/en/library/videos/intros-for-the-ministry/jehovahs-witnesses-who-are-we-intro permanent;',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => package['nginx'],
}
