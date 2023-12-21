bin/kafka-topics.sh --zookeeper localhost:9092 --delete --topic turbine2

./bin/kafka-topics.sh --delete --topic turbine1 --bootstrap-server localhost:9092
./bin/kafka-topics.sh --delete --topic turbine2 --bootstrap-server localhost:9092
./bin/kafka-topics.sh --delete --topic turbine3 --bootstrap-server localhost:9092
./bin/kafka-topics.sh --delete --topic turbine4 --bootstrap-server localhost:9092
./bin/kafka-topics.sh --delete --topic turbine5 --bootstrap-server localhost:9092

./bin/kafka-topics.sh --create --topic turbine1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
./bin/kafka-topics.sh --create --topic turbine2 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
./bin/kafka-topics.sh --create --topic turbine3 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
./bin/kafka-topics.sh --create --topic turbine4 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
./bin/kafka-topics.sh --create --topic turbine5 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1