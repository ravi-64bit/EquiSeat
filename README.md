# EquiSeat

EquiSeat is a small Flask application for managing exam rooms, student records and subjects, registering students for exams, and generating printable seating-plan PDFs.

## Requirements

- Python 3.10 or newer
- MySQL 8 or MariaDB 10.4+
- A database named `equiseat`

## 1. Get the project

```bash
git clone https://github.com/ravi-64bit/EquiSeat.git
cd EquiSeat
```

To use the repaired version, check out the `restore-working-app` branch:

```bash
git checkout restore-working-app
```

## 2. Create the database

For a new, empty database, run the setup schema:

```bash
mysql -u root -p < database/schema.sql
```

For the sample data from the original college project, create the database and import the original dump instead:

```bash
mysql -u root -p -e "CREATE DATABASE equiseat CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root -p equiseat < equiseat.sql
```

Use one setup path or the other; do not import both into the same database. The original dump contains sample records, while `database/schema.sql` creates an empty database.

## 3. Install Python dependencies

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Configure the database connection

The default local settings are:

| Setting | Default |
| --- | --- |
| Host | `localhost` |
| Port | `3306` |
| User | `root` |
| Password | empty |
| Database | `equiseat` |

Override them with environment variables when needed.

Windows PowerShell:

```powershell
$env:DB_HOST = "localhost"
$env:DB_PORT = "3306"
$env:DB_USER = "root"
$env:DB_PASSWORD = "your-password"
$env:DB_NAME = "equiseat"
```

macOS / Linux:

```bash
export DB_HOST=localhost
export DB_PORT=3306
export DB_USER=root
export DB_PASSWORD='your-password'
export DB_NAME=equiseat
```

## 5. Run EquiSeat

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

The app provides pages to manage rooms, add or import students, maintain subjects, register exams, and generate seating PDFs. Generated PDFs are stored in the local `generated/` folder and can be downloaded from the seating page.

## Student import format

CSV and Excel imports must include these column headings:

- `regd_no`
- `name`
- `section`

Each row represents one student. Subject registrations are added separately on the Subjects & Registrations page. To generate a seating plan, students must have at least one exam registration.

## Notes

- The seating generator places students with no shared registered subject next to one another where possible. If the constraints cannot all be satisfied, it still fills the available seats and checks room capacity.
- Keep the database credentials in environment variables; do not commit real passwords.
- `main.py` is the old experimental desktop interface. The maintained application entry point is `app.py`.
