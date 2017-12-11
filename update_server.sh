source bin/activate &&
python manage.py makemigrations &&
python manage.py migrate &&
mod_wsgi-express setup-server --https-only --log-level debug --server-name gestion.osl.ull.es --user www-data --group www-data --server-root /var/www/gespai --document-root /var/www/gespai --port 80 --https-port 443 --ssl-certificate-chain-file /etc/letsencrypt/live/gestion.osl.ull.es/chain.pem --ssl-certificate-file /etc/letsencrypt/live/gestion.osl.ull.es/cert.pem --ssl-certificate-key-file /etc/letsencrypt/live/gestion.osl.ull.es/privkey.pem gespai/wsgi.py
