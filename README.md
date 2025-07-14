# PetStore API Automation

## 🧪 Tech Stack

- Python 3.9
- Pytest
- Requests
- Pytest-HTML
- Flaky (for retry on unstable endpoints)
- Built-in logging via `pytest.ini`


## 🚀 Setup Instructions

1. Create virtual environment:
```bash
python3.9 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest
```