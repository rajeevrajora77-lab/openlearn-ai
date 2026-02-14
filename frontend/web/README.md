# OpenLearn Web Frontend

Next.js web application for OpenLearn AI.

## Tech Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **TailwindCSS** - Styling
- **tRPC** - End-to-end type-safe APIs
- **React Query** - Data fetching and caching

## Getting Started

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## Project Structure

```
app/
├── (auth)/          # Authentication pages
├── (dashboard)/     # Dashboard pages
├── api/             # API routes
├── layout.tsx       # Root layout
└── page.tsx         # Home page

components/
├── ui/              # Reusable UI components
├── features/        # Feature-specific components
└── layouts/         # Layout components

lib/
├── trpc/            # tRPC configuration
├── utils/           # Utility functions
└── hooks/           # Custom React hooks
```

## Coming Soon

Full frontend implementation with:
- User authentication flow
- AI tutor chat interface
- Mock test platform
- Progress dashboard
- Voice learning interface
