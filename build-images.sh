# -- Building the Images

sudo docker build -f cluster-base -t cluster-base .

sudo docker build -f spark-base -t spark-base .

sudo docker build -f spark-leader -t spark-leader .

sudo docker build -f spark-worker -t spark-worker .

sudo docker build -f pyspark-notebook -t pyspark-notebook .