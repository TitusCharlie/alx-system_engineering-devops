# Install and configure Nginx server

class web_server {
  
  # Install Nginx package
  package { 'nginx':
    ensure => present,
  }

  # Configure Nginx to listen on port 80
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
      listen 80;
      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }",
  }

  # Enable the default site
  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
  }

  # Restart Nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }

}

# Apply the web_server class
include web_server

