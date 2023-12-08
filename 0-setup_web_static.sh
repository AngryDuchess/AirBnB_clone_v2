#!/usr/bin/env bash
# Some comment

apt-get update
apt-get install nginx -y

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

echo "$fake_html" | tee "$root_dir/releases/test/index.html" > /dev/null

rm -r  "$root_dir/current"
ln -sf "$root_dir/releases/test" "$root_dir/current"

chown -Rh "siaw:siaw" "/data/"

nginx_loc="/etc/nginx/sites-available/default"

sed -i "/server_name _;/a\\        location /hbnb_static/ {alias $root_dir/current/;}" "$nginx_loc" > /dev/null

service nginx restart