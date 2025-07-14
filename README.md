# PetStore API Automation

👉 [Click here to view test-report.html](https://clashergeek77.github.io/ClasherGeek77/test-report.html)


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
export PYTHONPATH=your-path-to-folder
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