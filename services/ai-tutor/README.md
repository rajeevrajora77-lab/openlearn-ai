# AI Tutor Service

RAG-powered AI tutoring service for OpenLearn AI.

## Features

- RAG pipeline with hybrid retrieval
- Semantic caching
- Multi-language support
- Content moderation
- RAGAS evaluation

## Architecture

```
Query → Preprocessing → Semantic Cache → Hybrid Retrieval → 
Reranking → LLM Generation → Content Moderation → Response
```

## Endpoints

```
POST /api/v1/ai-tutor/query - Query the AI tutor
POST /api/v1/ai-tutor/feedback - Submit feedback
GET /api/v1/ai-tutor/history - Get chat history
```

## Performance Targets

- Latency (P95): < 2 seconds
- Accuracy (RAGAS): > 85%
- Cache hit rate: 40-50%

## Coming Soon

Full implementation with vLLM integration.
