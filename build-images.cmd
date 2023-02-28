::# -- Building the Images

start /b "" docker build -f cluster-base -t cluster-base .

start /b "" docker build -f spark-base -t spark-base .

start /b "" docker build -f spark-leader -t spark-leader .

start /b "" docker build -f spark-worker -t spark-worker .

start /b "" docker build -f pyspark-notebook -t pyspark-notebook .