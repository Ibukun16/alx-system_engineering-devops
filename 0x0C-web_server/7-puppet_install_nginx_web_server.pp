# Automate Installation of nginx server on ubuntu web-01 server us puppet manifest
# Nginx should be listening on port 80
# Return a page that contains "Hello World" when querying
# Nginx at its root with Get request using curl
# Configure your Nginx server so that /redirect_me is redirecting to another page.
# The redirection must be a “301 Moved Permanent


package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/github.com\/Ibukun16;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
