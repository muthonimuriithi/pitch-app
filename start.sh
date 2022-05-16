export DATABASE_URI='postgresql+psycopg2://muriithi:muthoni@localhost/pitches'
export MAIL_USERNAME='loisemuthoni181@gmail.com'
export MAIL_PASSWORD='0725408650'
export SECRET_KEY='secret'

# python3 run.py shell

python3 manage.py server


# python run.py db init
# python run.py db migrate -m "Initial Migration"
# python run.py db upgrade
