import pyspark
import os
import sys
from pyspark.sql import SQLContext

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


def test(text: str):
    # Use a breakpoint in the code line below to debug your script.
    sc = pyspark.SparkContext()
    sqlContext = SQLContext(sc)
    columns = ["vehicle_id", "timestamp", "latitude", "longitude"]
    values = [

        ['vehicle_1', '6546923651', '40.20', '30.10'],
        ['vehicle_2', '6546923651', '40.10', '30.10'],
        ['vehicle_1', '6546923652', '40.30', '30.20'],
        ['vehicle_2', '6546923652', '40.20', '30.20'],
        ['vehicle_1', '6546923653', '40.40', '30.30'],
        ['vehicle_2', '6546923653', '40.30', '30.30'],

    ]

    df = sqlContext.createDataFrame(values, columns)
    df.show()
    print(f'{text}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test('Test Test')
