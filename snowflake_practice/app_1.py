import snowflake.connector as sf



# aws account id : 
conn = sf.connect(
    user='Boinegoutham10',
    password='Goutham@1005',
    account='UE41703.ap-south-1',
    warehouse='compute_wh',
    database='customer_data'
)

with conn.cursor() as cur:
    cur.execute("select * from data")

    result_batch_list = cur.get_result_batches()

    num_result_batches = len(result_batch_list)

    for i in result_batch_list:
        for row in i:
            print(row)