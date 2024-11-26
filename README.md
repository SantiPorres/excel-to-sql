### Commands

```bash
docker build -t excel-to-sql .
```


```bash
# Generate SQL Statements
docker run --rm -v /path/to/your/data.xlsx:/app/data.xlsx -v ./output:/app/output excel-to-sql

# Execute SQL Statements in database
docker run --rm --net=host --env-file .env -v /path/to/your/data.xlsx:/app/data.xlsx excel-to-sql
```