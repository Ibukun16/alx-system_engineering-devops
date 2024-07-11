# Automating the installation of nginx web server using puppet manifest

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

service { 'nginx':
  ensure  => 'running',
  require => file_line['perform a redirection'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx']
}

file_line { 'perform a redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me/$ https://www.jw.org/en/library/videos/intros-for-the-ministry/jehovahs-witnesses-who-are-we-intro permanent;',
  after   => 'root /var/www/html;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
