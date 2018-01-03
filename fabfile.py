#
# Executes the project via Fabric
#

from fabric.api import local, env, run
from fabric.context_managers import lcd

#
# Packaging
#

def package():
    print("Packaging all Scala Projects into JAR files")
    package_tf_idf()
    package_query_engine()

def package_tf_idf():
    print("Packaging TF-IDF into JAR files...")
    with lcd('GenerateTfIdf/'):
        local("sbt clean package")

def package_query_engine():
    print("Packaging all Query Engine into JAR file...")
    with lcd('QueryEngine/'):
        local("sbt clean package")

#
# Execution
#

def run_tf_idf():
    print("[MAIN] Sumbitting job to Spark for Generating TF-IDF...")
    with lcd('GenerateTfIdf/'):
        local("spark-submit target/scala-2.10/generatetfidf_2.10-1.0.0-SNAPSHOT.jar --main >> logs/spark.log 2>&1 &", pty=False)

def run_sample_tf_idf():
    print("[SAMPLE] Sumbitting job to Spark for Generating TF-IDF...")
    with lcd('GenerateTfIdf/'):
        local("spark-submit target/scala-2.10/generatetfidf_2.10-1.0.0-SNAPSHOT.jar --sample >> logs/spark.log 2>&1 &", pty=False)

def run_query_engine():
    print("[MAIN] Sumbitting job to Spark for Query Engine...")
    query = prompt("Query?")
    with lcd('QueryEngine/'):
        local("spark-submit target/scala-2.10/queryengine_2.10-1.0.0-SNAPSHOT.jar --main \"%s\" >> logs/spark.log 2>&1 &" % (query), pty=False)

def run_sample_query_engine():
    print("[SAMPLE] Packaging all Query Engine into Query Engine...")
    query = prompt("Query?")
    with lcd('QueryEngine/'):
        local("spark-submit target/scala-2.10/queryengine_2.10-1.0.0-SNAPSHOT.jar --sample \"%s\" >> logs/spark.log 2>&1 &" % (query), pty=False)

#
# HDFS Commands
#

def hdfs_ls_query_engine():
    print("Listing files in HDFS in spark-search-eninge...")
    local("hadoop fs -ls /user/mnf30")

def hdfs_check_quota():
    print("HDFS: Quota")
    local("hdfs dfs -count -q -h /user/mnf30")