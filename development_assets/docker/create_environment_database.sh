#/bin/bash

docker exec -t table_to_database_database <<EOF
mysql -uroot -pstronggpassword -e "CREATE DATABASE table_to_database_test;"
EOF
