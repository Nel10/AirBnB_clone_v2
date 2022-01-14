# setup web static

exec { 'configure everything':
    command  => 'sudo apt-get -y update && sudo apt-get -y upgrade && sudo apt-get -y install nginx && sudo ufw allow 'Nginx HTTP' && sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/ && echo "<html><head></head><body>Holberton School</body></html>" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -hR ubuntu:ubuntu /data/ && str="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" && sudo sed -i "24i $str" /etc/nginx/sites-available/default && sudo service nginx reload && sudo service nginx start',
    provider => shell,
}
