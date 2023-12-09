# TODO: Importations
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import sum, max, min

# TODO: Create App
spark = SparkSession.builder.appName('Hello World').getOrCreate()

# Create columns
columns = [
    Row(nomes='Who', index=1, color='brown'),
    Row(nomes='Cria', index=2, color='blue'),
    Row(nomes='Capetão', index=3, color='yellow')
]

# TODO: Create DataFrame
df = spark.createDataFrame(columns) 

# TODO: Filter min number
small = df.agg(min(df.index).alias('Menor número'))
print(small.show(truncate=True))

# TODO: Filter max number
big = df.agg(max(df.index).alias('Maior número'))
print(big.show())

# TODO: Return table
flt = df.filter(df.index == 1)
flt.show()

# TODO: Search specify colum
df.select("artists") Printar apenas uma coluna

# TODO: All informations
df.show() 
