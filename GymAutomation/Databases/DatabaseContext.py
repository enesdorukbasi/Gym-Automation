import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "GymAutomationDB",
    user = "postgres",
    password = "12345"
)