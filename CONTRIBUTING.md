# Contributing to FoodSafe

## Security Issues

**DO NOT** open a GitHub issue for security vulnerabilities.

Instead, email: security@foodsafe.example.com

We'll respond within 48 hours and coordinate a fix before public disclosure.

## Bug Reports

1. Check existing issues first
2. Include: OS, Python version, error trace
3. Steps to reproduce
4. Expected vs actual behavior

## Pull Requests

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open a PR

## Code Standards

- Python 3.11+ type hints
- Pydantic v2 for schemas
- SQLAlchemy 2.0 ORM only
- Black + isort formatting
- pytest for tests

## Testing

```bash
cd backend
pytest tests/ -v
```

## Pre-Commit

- [ ] Code compiles without errors
- [ ] Tests pass
- [ ] Security scan clean
- [ ] Documentation updated
