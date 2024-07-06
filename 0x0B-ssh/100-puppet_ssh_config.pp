# A Puppet script that creates ssh config file
include stdlib

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	 PasswordAuthenticatication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	 IdentityFile ~/.ssh/school',
  replace => true,
}
