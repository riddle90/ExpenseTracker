# Local-First Expense Tracker 🛡️

A privacy-focused, desktop-based expense tracker that processes bank statements (CSV/PDF) locally on your machine. It uses a hybrid categorization engine (Rules + LLM) to classify transactions without exposing your financial history to the cloud.

## 🏗 Architecture

- **Frontend**: Flutter (Desktop - macOS/Windows)
- **Backend**: Python (FastAPI)
- **Database**: SQLite (Local storage)
- **Data Processing**: Pandas (CSV/Excel ingestion)
- **AI Layer**: Optional LLM integration (OpenAI/Gemini) for unknown vendors.

## 🚀 Features

- **100% Privacy**: Your bank account numbers and transaction amounts never leave your device. Only sanitized merchant names are sent to the LLM (if enabled) for categorization.
- **Smart Caching**: Learns from your history. "STARBUCKS #123" is categorized once, then cached locally forever.
- **Universal Ingestion**: Drag-and-drop support for CSVs, Excel, and PDFs.
- **Interactive Dashboard**: Visual breakdown of spending by category and month.

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.9+
- Flutter SDK
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/riddle90/ExpenseTracker
cd ExpenseTracker
```

### 2. Backend Setup (Python)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000

### 3. Frontend Setup (Flutter)

Open a new terminal:

```bash
cd frontend
flutter pub get
flutter run -d macos  # or windows
```

## 📂 Project Structure

```
expense_tracker_local/
├── backend/            # Python FastAPI Server & Logic
│   ├── main.py         # API Entry point
│   ├── processors/     # CSV/PDF parsing logic
│   └── db/             # SQLite connection & schema
├── frontend/           # Flutter Desktop App
│   ├── lib/
│   │   ├── screens/    # Dashboard, Upload, Settings UI
│   │   └── services/   # API connectors
├── data/               # Local storage (GitIgnored)
└── README.md
```

## 🔒 Privacy Guarantee

This application follows a "Local-First" philosophy:

- **Ingestion**: Happens entirely in Python on your CPU.
- **Storage**: Data is stored in expenses.db on your hard drive.
- **LLM Usage**: If an API key is provided, only the Merchant Name (e.g., "AMZN MKTP") is sent to the cloud to determine the category. Dates, amounts, and account IDs are stripped before the request is made.
