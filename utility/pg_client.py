from typing import List
import psycopg2

from utility.creds import credentials as cred

TRANSACTION_SIZE = 1000



class PgClient:

    def __init__(self):
        self.conn = psycopg2.connect(**cred['pg'])
    

    def insert_rows_to_table(
        self,
        data: List[tuple],
        columns: List[str],
        table_name: str
        ) -> None:

        import psycopg2.extras as ex
        
        with self.conn.cursor() as cur:
            chunked_tuples = [
                data[i:i+TRANSACTION_SIZE]
                for i in range(0, len(data), TRANSACTION_SIZE)
            ]

            req_str = f"INSERT INTO {table_name} ({','.join(columns)}) values %s"

            for i, chunk in enumerate(chunked_tuples):
                ex.execute_values(cur,req_str,chunk)

                self.conn.commit()
                print(f'inserted {len(chunk)} values into table {table_name}')


    def sql_exec(self, sql_str: str) -> List[tuple]:
        with self.conn.cursor() as cur:
            cur.execute(sql_str)
            return cur.fetchall()