# Personal Finance Crisis API

API-driven solution for personal financial management, debt tracking, and AI-powered financial advice.

## Features

- 🔐 Secure authentication and user profiles
- 💰 Budget creation and management
- 💳 Debt tracking and payoff strategies
- 📊 Transaction analysis and categorization
- 🤖 AI-powered financial advice
- 📈 Financial reports and insights

## Tech Stack

- Django Rest Framework
- GPT-4 Integration
- PostgreSQL
- JWT Authentication
- Celery for async tasks

## Installation

```bash
git clone https://github.com/DavidDanso/personal-finance-crisis-api.git
cd personal-finance-crisis-api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment Variables

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
OPENAI_API_KEY=your-openai-key
```

## API Documentation

### Authentication
Control user access and security.

- `POST /api/auth/register/`: Create new user account
- `POST /api/auth/login/`: Obtain JWT token
- `POST /api/auth/logout/`: Invalidate token
- `POST /api/auth/reset-password/`: Reset user password

### User Profile
Manage user information and preferences.

- `GET /api/users/profile/`: Retrieve user profile
- `PUT /api/users/profile/`: Update entire profile
- `PATCH /api/users/profile/`: Partial profile update
- `POST /api/users/profile/upload-transactions/`: Bulk upload transactions

### Budget Management
Create and track budgets.

- `GET /api/budgets/`: List all budgets
- `POST /api/budgets/`: Create new budget
- `GET /api/budgets/{id}/`: Get budget details
- `PUT /api/budgets/{id}/`: Update budget
- `DELETE /api/budgets/{id}/`: Remove budget
- `POST /api/budgets/{budget_id}/categories/`: Add new category to budget
- `POST /api/budgets/{budget_id}/categories/{id}/transactions/`: Add transaction to category

### Debt Management
Track and analyze debts.

- `GET /api/debts/`: List all debts
- `POST /api/debts/`: Add new debt
- `GET /api/debts/{id}/`: Get debt details
- `PUT /api/debts/{id}/`: Update debt
- `DELETE /api/debts/{id}/`: Remove debt
- `GET /api/debts/{id}/payoff-plan/`: Get debt payoff strategies
- `POST /api/debts/consolidation-analysis/`: Analyze debt consolidation options

### Transaction Analysis
Analyze spending patterns.

- `GET /api/transactions/`: List transactions
- `POST /api/transactions/bulk-upload/`: Bulk import transactions
- `GET /api/transactions/analysis/`: Get spending analysis
- `GET /api/transactions/categories/`: List transaction categories
- `GET /api/transactions/export/`: Export transactions

### AI Assistant
Get AI-powered financial advice.

- `POST /api/assistant/chat/`: Get personalized financial advice
- `POST /api/assistant/budget-advice/`: Get budget optimization tips
- `POST /api/assistant/debt-advice/`: Get debt management strategies
- `GET /api/assistant/saved-advice/`: Access previous advice

### Reports
Generate financial insights.

- `GET /api/reports/spending-patterns/`: Analyze spending trends
- `GET /api/reports/debt-analysis/`: Comprehensive debt analysis
- `GET /api/reports/budget-performance/`: Track budget performance
- `GET /api/reports/export/{report_type}/`: Export specific reports

## Authentication

All API endpoints except registration and login require JWT authentication:

```bash
curl -H "Authorization: Bearer your-token" https://api-url/endpoint
```

## Response Formats

Success Response:
```json
{
    "status": "success",
    "data": {
        "key": "value"
    }
}
```

Error Response:
```json
{
    "status": "error",
    "message": "Error description",
    "code": "ERROR_CODE"
}
```

## Rate Limiting

- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -am 'Add feature'`)
4. Push branch (`git push origin feature/name`)
5. Create Pull Request

Happy Coding🎉
