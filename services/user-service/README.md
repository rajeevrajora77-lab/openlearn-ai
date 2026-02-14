# User Service

User profile and progress tracking service for OpenLearn AI.

## Features

- User profile management
- Learning progress tracking
- Subscription management
- Analytics events

## Endpoints

```
GET /api/v1/users/{id}/profile - Get user profile
PUT /api/v1/users/{id}/profile - Update profile
GET /api/v1/users/{id}/progress - Get learning progress
POST /api/v1/users/{id}/progress - Update progress
```

## Coming Soon

Full implementation following the auth-service pattern.
