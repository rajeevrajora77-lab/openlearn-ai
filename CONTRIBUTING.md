# Contributing to OpenLearn AI

Thank you for your interest in contributing to OpenLearn AI! 🎉

We welcome contributions from developers, educators, students, and anyone passionate about improving education technology.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful, inclusive, and constructive in all interactions.

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what's best for the community
- ✅ Show empathy towards other community members
- ❌ No harassment, discrimination, or inappropriate behavior

---

## How Can I Contribute?

### 🐛 Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/rajeevrajora77-lab/openlearn-ai/issues)
2. If not, create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, browser, versions)
   - Screenshots/logs if applicable

### ✨ Suggesting Features

1. Check existing [Feature Requests](https://github.com/rajeevrajora77-lab/openlearn-ai/labels/enhancement)
2. Create a new issue with:
   - Clear use case
   - Why this feature would be valuable
   - Proposed implementation (optional)

### 🔧 Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Write tests**
5. **Run linters and tests**
   ```bash
   # Python
   black services/
   flake8 services/
   pytest tests/
   
   # TypeScript
   npm run lint
   npm run test
   ```
6. **Commit with conventional commits**
   ```bash
   git commit -m "feat: add new feature"
   ```
7. **Push and create a pull request**

### 📝 Documentation

- Improve existing documentation
- Add code examples
- Translate documentation to other languages
- Create tutorials and guides

### 🌍 Translations

Help make OpenLearn accessible to more students:

1. Check existing translations in `locales/`
2. Add new language files
3. Translate UI strings
4. Review and improve existing translations

---

## Development Setup

### Prerequisites

- Docker >= 24.0
- Docker Compose >= 2.20
- Python >= 3.11
- Node.js >= 20.0
- Git

### Initial Setup

```bash
# 1. Clone your fork
git clone https://github.com/YOUR_USERNAME/openlearn-ai.git
cd openlearn-ai

# 2. Add upstream remote
git remote add upstream https://github.com/rajeevrajora77-lab/openlearn-ai.git

# 3. Start development environment
docker-compose -f docker-compose.dev.yml up -d

# 4. Install dependencies
# Backend
cd services/auth-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Frontend
cd ../../frontend/web
npm install

# 5. Run migrations
docker-compose exec auth-service alembic upgrade head

# 6. Start development servers
# Backend (in separate terminals)
cd services/auth-service && uvicorn src.main:app --reload
cd services/ai-tutor && uvicorn src.main:app --reload --port 9001

# Frontend
cd frontend/web && npm run dev
```

### Running Tests

```bash
# Unit tests
pytest tests/unit/ -v --cov=services/

# Integration tests
pytest tests/integration/ -v

# Load tests
k6 run tests/load/rag_load_test.js
```

---

## Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)

### PR Description Template

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #123

## How Has This Been Tested?
- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## Screenshots (if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing
```

### Review Process

1. **Automated Checks** - CI/CD pipeline must pass
2. **Code Review** - At least one maintainer approval required
3. **Testing** - Reviewer tests the changes
4. **Merge** - Squash and merge to main branch

---

## Coding Standards

### Python

- **Style**: Follow [PEP 8](https://pep8.org/)
- **Formatter**: Black (line length: 100)
- **Linter**: Flake8
- **Type Hints**: Use type annotations
- **Docstrings**: Google style

```python
def process_query(query: str, context: dict) -> dict:
    """Process a user query through the RAG pipeline.
    
    Args:
        query: The user's question
        context: Additional context (exam_id, subject_id, etc.)
    
    Returns:
        dict: Response with 'answer' and 'sources' keys
    
    Raises:
        ValueError: If query is empty
    """
    pass
```

### TypeScript/JavaScript

- **Style**: Follow [Airbnb Style Guide](https://github.com/airbnb/javascript)
- **Formatter**: Prettier
- **Linter**: ESLint
- **Type Safety**: Use TypeScript strict mode

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add voice recognition feature
fix: resolve authentication bug
docs: update API documentation
test: add unit tests for RAG pipeline
refactor: optimize database queries
chore: update dependencies
```

---

## Testing

### Test Coverage Requirements

- **Unit Tests**: 70% minimum coverage
- **Integration Tests**: Critical flows covered
- **E2E Tests**: User journeys tested

### Writing Tests

```python
# tests/unit/test_rag_pipeline.py
import pytest
from unittest.mock import AsyncMock
from services.ai_tutor.rag_pipeline import RAGPipeline

@pytest.mark.asyncio
async def test_semantic_caching():
    """Test that cached responses are returned without LLM call"""
    pipeline = RAGPipeline()
    pipeline.llm = AsyncMock()
    
    # First call - cache miss
    result1 = await pipeline.process_query("test query")
    assert pipeline.llm.called
    
    # Second call - cache hit
    pipeline.llm.reset_mock()
    result2 = await pipeline.process_query("test query")
    assert not pipeline.llm.called
    assert result1 == result2
```

---

## Documentation

### What to Document

- **API Endpoints**: OpenAPI/Swagger specs
- **Architecture**: System design decisions
- **Configuration**: Environment variables, settings
- **Runbooks**: Operational procedures
- **Tutorials**: Step-by-step guides

### Documentation Structure

```
docs/
├── architecture/     # System design
├── api/             # API reference
├── deployment/      # Deployment guides
├── development/     # Developer guides
└── tutorials/       # User tutorials
```

---

## Getting Help

- **GitHub Discussions**: Ask questions
- **Discord**: Real-time chat
- **Email**: tech@openlearn.ai

---

## Recognition

Contributors are recognized in:
- GitHub Contributors page
- Monthly contributor spotlight
- Annual report

---

**Thank you for contributing to OpenLearn AI! Together, we're making education accessible to millions of students.** 🙏
