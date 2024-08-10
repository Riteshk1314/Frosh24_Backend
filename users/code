import csv
import psycopg2
from psycopg2 import sql
import logging
import random
import string

# Database connection parameters
db_params = {
    'dbname': 'defaultdb',
    'user': 'doadmin',
    'password': 'AVNS_xUR4qeB4uoxTyYcpnvq',
    'host': 'db-postgresql-blr1-29858-do-user-13808581-0.f.db.ondigitalocean.com',
    'port': '25060',
}

# CSV file path
csv_file_path = 'fresher.csv'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to generate a random password
def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to generate a random 8-digit secure ID
def generate_random_secure_id(length=8):
    digits = string.digits
    secure_id = ''.join(random.choice(digits) for i in range(length))
    return secure_id

# Function to insert data into the database
def insert_user_data(conn, name, registration_id, email, image_path, is_active, is_superuser, password, secure_id, events):
    with conn.cursor() as cur:
        query = sql.SQL("""
            INSERT INTO "users_user" (name, registration_id, email, image, is_active, is_superuser, password, secure_id, events)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """)
        cur.execute(query, (name, registration_id, email, image_path, is_active, is_superuser, password, secure_id, events))

# Main function to read CSV and insert data
def main():
    conn = None
    try:
        logging.info("Attempting to connect to the database...")
        conn = psycopg2.connect(**db_params)
        logging.info("Successfully connected to the database.")
        
        logging.info(f"Opening CSV file: {csv_file_path}")
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row
            
            for row_num, row in enumerate(csvreader, start=2):  # Start from 2 to account for header
                if len(row) != 4:
                    logging.warning(f"Row {row_num} has {len(row)} columns instead of 4: {row}")
                    continue
                name, registration_id, email, image_path = row
                # Set is_active and is_superuser to False by default
                is_active = False
                is_superuser = False
                # Generate a random password and secure ID
                password = generate_random_password()
                secure_id = generate_random_secure_id()
                # Set default values for events
                events = []
                # Log the generated values
                logging.info(f"Generated values for row {row_num}: password={password}, secure_id={secure_id}")
                try:
                    insert_user_data(conn, name, registration_id, email, image_path, is_active, is_superuser, password, secure_id, events)
                    conn.commit()  # Commit after every successful insert
                except psycopg2.Error as e:
                    logging.error(f"Error inserting row {row_num}: {e}")
                    conn.rollback()  # Rollback the transaction on error
        
        logging.info("Data insertion completed")

    except (Exception, psycopg2.Error) as error:
        logging.error(f"An error occurred: {error}")
        if conn:
            conn.rollback()
    
    finally:
        if conn:
            conn.close()
            logging.info("Database connection closed.")
        else:
            logging.warning("No database connection was established.")

if __name__ == "__main__":
    main()
