import PoolWithMySQL1

class Temp(PoolWithMySQL1):

    def query(self,select,table, full_string=None):
        if not full_string:
            full_string = "SELECT %s FROM %s" % (select,table)

        cnx  = self.cnxpool.get_connection()

        cursor = cnx.cursor(buffered=True)

        cursor.execute(full_string)

        desc = cursor.description
        column_names = [col[0] for col in desc]

        data = [dict(zip(column_names, row)) for row in cursor.fetchall()]

        cursor.close()

        cnx.close()

        return data
    
t = Temp()
print(t.query("*","user_details", full_string=None))
