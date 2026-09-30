import os
import mysql.connector

DB_HOST = os.environ.get("DBHOST")
DB_NAME = os.environ.get("DBNAME")
DB_USER = os.environ.get("DBUSER")
DB_PASSWORD = os.environ.get("DBPASS")
CSV_FILE = "MOCK_DATA.csv"

db = mysql.connector.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = db.cursor()

def get_data_by_group(value):
    """Return MOCK_DATA rows whose `group` column value matches value parameter."""
    query = "SELECT * FROM mock WHERE `group` = %s;"
    try:
        cur.execute(query, (value,))
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        return output
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return None

def plot_counts(groupby):
    """Return the number of rows for each distinct value in the groupby column."""
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"
    cur.execute(query)
    results = cur.fetchall()
    output = []
    for r in results:
            output.append(r)
    return output

def main():
    """Run the demo queries and close the database connection."""

    print("=== by group ===")
    print(get_data_by_group("A"))

    print("=== counts ===")
    print(plot_counts("gender"))

    cur.close()
    db.close()



if __name__ == "__main__":
    main()