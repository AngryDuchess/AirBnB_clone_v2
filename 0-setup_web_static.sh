#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y

root_dir="/data/web_static"
mkdir -p "$root_dir/releases/test"
mkdir -p "$root_dir/shared"

fake_html="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$fake_html" | tee "$root_dir/releases/test/index.html" >/dev/null

rm -r "$root_dir/current"
ln -sf "$root_dir/releases/test" "$root_dir/current"

chown -Rh "ubuntu:ubuntu" "/data/"

nginx_cfg="/etc/nginx/sites-available/default"
sed -i "/server_name _;/a\\         location /hbnb_static/ {alias $root_dir/current/;}" "$nginx_cfg" > /dev/null

sudo service nginx restart