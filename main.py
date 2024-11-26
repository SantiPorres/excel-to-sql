import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2
import os
import json

file_path = "data.xlsx"
df = pd.read_excel(file_path, engine="openpyxl", header=None)


# GENERATE SQL STATEMENTS

sql_statements = []
for index, row in df.iterrows():
    identifier = int(row[0])
    column_b_value = float(row[1])
    column_c_value = float(row[2])

    update_query = f"""
    UPDATE table_name
    SET column1 = {column_b_value},
        column2 = {column_c_value}
    WHERE id = {identifier};
    """

    sql_statements.append(update_query)

output_file = "/app/output/generated_sql_statements.sql"
with open(output_file, "w") as f:
    for statement in sql_statements:
        f.write(statement)
        f.write("\n")


print(f"SQL file '{output_file}' has been created with {len(sql_statements)} statements.")


# EXECUTE SQL STATEMENTS IN DATABASE

# db_name = os.getenv('DB_NAME')
# db_user = os.getenv('DB_USER')
# db_password = os.getenv('DB_PASSWORD')
# db_host = os.getenv('DB_HOST')
# db_port = os.getenv('DB_PORT')


# connection_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# engine = create_engine(connection_url)

# successful_rows = 0

# for index, row in df.iterrows():
#     identifier = int(row[0])
#     column_b_value = float(row[1])
#     column_c_value = float(row[2])

#     update_query = text("""
#     UPDATE table_name
#     SET column1 = :column1,
#         column2 = :column2
#     WHERE id = :id;
#     """)

    # with engine.connect() as connection:
    #     params = {
    #         'column1': column_b_value,
    #         'column2': column_c_value,
    #         'id': identifier
    #     }
        
    #     # Debugging
    #     # print(update_query)
    #     # print(json.dumps(params, indent=4))
    #     # print('------------------------------------------------------------')

    #     connection.execute(update_query, params)
    #     successful_rows += 1

# print("Update completed.")
# print(f"Total rows updated: {successful_rows}")
