import sqlite3

# ---------------- Database Setup ----------------
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    ailment TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialty TEXT,
    schedule TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    amount REAL,
    status TEXT,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
)
''')
conn.commit()

# ---------------- Functions ----------------
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender (M/F): ")
    ailment = input("Enter patient ailment: ")
    cursor.execute("INSERT INTO patients (name, age, gender, ailment) VALUES (?, ?, ?, ?)",
                   (name, age, gender, ailment))
    conn.commit()
    print("✅ Patient added successfully!")

def view_patients():
    cursor.execute("SELECT * FROM patients")
    for row in cursor.fetchall():
        print(row)

def add_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter specialty: ")
    schedule = input("Enter schedule (e.g., Mon-Fri 9am-5pm): ")
    cursor.execute("INSERT INTO doctors (name, specialty, schedule) VALUES (?, ?, ?)",
                   (name, specialty, schedule))
    conn.commit()
    print("✅ Doctor added successfully!")

def view_doctors():
    cursor.execute("SELECT * FROM doctors")
    for row in cursor.fetchall():
        print(row)

def generate_bill():
    patient_id = int(input("Enter patient ID: "))
    amount = float(input("Enter bill amount: "))
    status = "Unpaid"
    cursor.execute("INSERT INTO bills (patient_id, amount, status) VALUES (?, ?, ?)",
                   (patient_id, amount, status))
    conn.commit()
    print("✅ Bill generated!")

def view_bills():
    cursor.execute("SELECT * FROM bills")
    for row in cursor.fetchall():
        print(row)

# ---------------- Menu ----------------
while True:
    print("\n🏥 Hospital Management System")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Add Doctor")
    print("4. View Doctors")
    print("5. Generate Bill")
    print("6. View Bills")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        add_doctor()
    elif choice == "4":
        view_doctors()
    elif choice == "5":
        generate_bill()
    elif choice == "6":
        view_bills()
    elif choice == "7":
        print("Exiting... Goodbye 👋")
        break
    else:
        print("❌ Invalid choice! Try again.")
