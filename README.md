# Flask Login & Registration App
**Developed by Arsh Sandhi | CR of 4AI1 Batch 2**

## 🚀 Setup & Run

### 1. Install Flask
```bash
pip install flask
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

## 📁 Structure
```
flask_auth_app/
├── app.py              ← Flask backend
├── users.json          ← Auto-created on first registration
├── requirements.txt
├── README.md
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

## ✅ Features
- Register with username + password (stored in users.json)
- Duplicate username prevention
- Login validation
- Session-based authentication
- Personalized welcome dashboard
- Flash messages for all errors/successes
- Logout support
