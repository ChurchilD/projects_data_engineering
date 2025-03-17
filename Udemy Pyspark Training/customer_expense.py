import os
os.environ['SPARK_HOME'] = 'C:\spark\spark-3.5.5-bin-hadoop3'
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jre1.8.0_202'
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("SpendByCustomer")
sc = SparkContext(conf = conf)

def extractCustomerPricePairs(line):
    fields = line.split(',')
    return (int(fields[0]), float(fields[2]))

input = sc.textFile("customer-orders.csv")
mappedInput = input.map(extractCustomerPricePairs)
totalByCustomer = mappedInput.reduceByKey(lambda x, y: x + y)

results = totalByCustomer.collect();
for result in results:
    print(result)