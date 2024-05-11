sed -i "s/#port = 5433/port = ${POSTGRES_PORT}/" /etc/postgresql/13/main/postgresql.conf

service postgresql restart

python app.py
