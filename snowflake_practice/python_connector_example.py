import snowflake.connector as sf

from python_veritas_base import python_veritas_base

class python_connector_example(python_veritas_base):

    def __init__(self):
        pass

    def do_the_real_work(self, conn):
        conn.cursor().execute("create or replace table test_table(col1 integer, col2 string)")

        conn.cursor().execute("insert into test_table(col1, col2) values(123,'goutham'),(456, 'sunny')")


        cur = conn.cursor()

        try:
            cur.execute("select * from test_table")
            for i in cur:
                print(i)
        except:
            cur.close()

    
if __name__ == "__main__":
    test_case = python_connector_example()
    test_case.main()