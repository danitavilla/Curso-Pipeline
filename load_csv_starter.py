import psycopg2
import os


def delete_records(conn, csv_file_path):
    # create the delete query
    delete_query = ""
    cur = conn.cursor()
    cur.execute(delete_query, (csv_file_path,))
    conn.commit()
    cur.close()


def load_csv_to_postgres(conn, csv_file_path):
    cur = conn.cursor()
    sql = ""
    cur.copy_expert(sql, open(csv_file_path, "r"))
    conn.commit()
    cur.close()


def main():
    print(-1)


if __name__ == "__main__":
    main()
