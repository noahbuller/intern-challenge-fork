# Javelin Sports Tech Intern Challenge

This repository contains the starter code for the Javelin Sports Tech intern coding challenge. Your task is to build a FastAPI backend that interacts with our AWS RDS database and to create the NextJS API integration layer.

## Project Structure

```
intern-challenge/
├── app/                    # FastAPI application
│   ├── core/               # Core modules (config, database)
│   ├── models/             # SQLAlchemy models (to be implemented)
│   ├── schemas/            # Pydantic schemas (to be implemented)
│   ├── api/                # API endpoints (to be implemented)
│   └── utils/              # Utility functions
├── config/                 # Configuration files
├── tests/                  # Test cases (optional but recommended)
└── nextjs-integration/     # NextJS integration (to be implemented)
```

## Getting Started

1. Clone this repository
2. Set up a virtual environment
3. Install dependencies
4. Configure your environment variables
5. Implement the required functionality

### Environment Setup

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create your .env file
cp .env.example .env
# Update the .env file with the provided credentials
```

### Database Connection

The project is configured to connect to a dummy AWS RDS PostgreSQL instance. The connection details are provided in the `.env.example` file. Make sure to update your `.env` file with the credentials provided separately.

The database schema is provided in `config/database_schema.json`. You can use this to understand the database structure and create your SQLAlchemy models.

### Running the Application

```bash
# Start the FastAPI application
uvicorn app.main:app --reload
```

## Your Tasks

### 1. Backend API (FastAPI)

Implement a FastAPI application that:

- Connects to the provided AWS RDS PostgreSQL database
- Retrieves athlete information
- Calculates weighted scores based on configuration
- Computes derived metrics (like athlete age)

### 2. Frontend API Integration (NextJS)

Create the NextJS API integration layer:

- Implement API route handlers in the NextJS app
- Create TypeScript interfaces for the data models
- Handle errors and state management

## Evaluation Criteria

Your solution will be evaluated based on:

- Code quality and organization
- API design
- Error handling
- Documentation
- Creativity and problem-solving

## Submission

Please email your completed solution to vidyut@javelinai.io as a ZIP file containing your project directory. Include a detailed README explaining your implementation and any design decisions you made.

Good luck!!

Vidyut
