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

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'Hello':
  command  => 'echo -e "Hello World!" | dd status=none of=/var/www/html/index.nginx-debian.html',
  provider => shell,

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.jw.org\/en\/library\/videos\/intros-for-the-ministry/jehovahs-witnesses-who-are-we-intro\/;\\n\\t}/" /etc/nginx/sites-enabled/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
