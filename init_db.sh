set -e

# Only run this from docker:
if [ -f /.dockerenv ]; then
    if psql -U $POSTGRES_USER -lqt | cut -d \| -f 1 | grep -qw $POSTGRES_DB; then
        echo "$POSTGRES_DB DB exists"
    else
        echo "$POSTGRES_DB doesnt exist"
    fi
    # echo "Database does not exist, creating 'compose_flask_boilerplate'"
    # psql -v ON_ERROR_STOP=1
    #     CREATE DATABASE compose_flask_boilerplate;
    #     CREATE USER root WITH ENCRYPTED PASSWORD 'boilerplate1234';
    #     GRANT ALL PRIVILEGES ON DATABASE root TO compose_flask_boilerplate;
    # EOSQL
fi