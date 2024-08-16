# A puppet manuscript to fix a broken line in a file on a server
#replace line containing "phpp" with "php"
exec{ 'fix-wordpress':
    command => "sudo sed -i \'s/.phpp/.php/g\' /var/www/html/wp-settings.php",
    path    => ['/bin','/usr/bin']
}
