set -e

# Only run this from docker:
if [ -f /.dockerenv ]; then
    if psql -U $POSTGRES_USER -lqt | cut -d \| -f 1 | grep -qw $POSTGRES_DB; then
        echo "$POSTGRES_DB DB exists"
    else
        echo "$POSTGRES_DB doesnt exist"
        echo "Database does not exist, creating '$POSTGRES_DB'"
        psql -v ON_ERROR_STOP=1
            CREATE DATABASE $POSTGRES_DB;
            CREATE USER root WITH ENCRYPTED PASSWORD $POSTGRES_PASSWORD;
            GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_USER TO $POSTGRES_DB;
        EOSQL
    fi
fi