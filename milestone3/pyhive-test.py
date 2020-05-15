from pyhive import hive

conn = hive.Connection(host="192.168.1.100", port=10000, auth="KERBEROS", database="bmdatalake", kerberos_service_name= "hive")

cursor = conn.cursor()

cursor.execute("select * from dl_his_kotesh limit 10")

for result in cursor.fetchall():
    use_result(result)