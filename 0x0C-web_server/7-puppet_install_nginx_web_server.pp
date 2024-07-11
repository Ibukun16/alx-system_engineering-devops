# Puppet manifest to automate the installation of nginx 
# Install nginx server on ubuntu web-01 server
# Nginx should be listening on port 80
# Return a page that contains "Hello World" when querying
# Nginx at its root with Get request using curl
# Configure your Nginx server so that /redirect_me is redirecting to another page.
# The redirection must be a “301 Moved Permanently”

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
