# Telangana AI–PrajaVani

## Day 2 — Repository Structure

### Purpose

The repository structure separates the application into clear modules so that schemas, APIs, services, data, models, and tests can be developed and maintained independently.

### Proposed Structure

```text
praja-vani/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── complaints.py
│   │   ├── classify.py
│   │   └── duplicate.py
│   ├── schemas/
│   │   └── complaint.py
│   ├── services/
│   │   ├── routing.py
│   │   ├── urgency.py
│   │   └── duplicate_detection.py
│   └── models/
│       └── complaint.py
├── data/
│   ├── train/
│   ├── validation/
│   └── demo/
├── tests/
│   ├── test_schema.py
│   ├── test_classify.py
│   └── test_duplicate.py
├── README.md
├── requirements.txt
└── .env.example 