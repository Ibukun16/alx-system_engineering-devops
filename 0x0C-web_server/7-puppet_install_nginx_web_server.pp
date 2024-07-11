# Puppet script to install nginx 
# Install nginx server on ubuntu web-01 server
# Nginx should be listening on port 80
# Return a page that contains "Hello World" when querying
# Nginx at its root with Get request using curl
# Configure your Nginx server so that /redirect_me is redirecting to another page.
# The redirection must be a “301 Moved Permanently”
# Configure your Nginx server to have a custom 404 page that
# contains the string Ceci n'est pas une page
# The page must return an HTTP 404 error code
# The page must contain the string Ceci n'est pas une page

exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

package { 'nginx':
  ensure => 'installed',
}

file_line { 'installed':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.jw.org/en/library/videos/intros-for-the-ministry/jehovahs-witnesses-who-are-we-intro permanent;'
}

file { 'var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'run':
  command  => 'sudo service nginx start',
  provider => shell,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
