set -e

# Only run this from docker:
if [ -f /.dockerenv ]; then
    if psql -U $POSTGRES_USER -lqt | cut -d \| -f 1 | grep -qw $POSTGRES_DB; then
        echo "$POSTGRES_DB DB exists"
    else
        echo "$POSTGRES_DB doesnt exist"
    fi
fi