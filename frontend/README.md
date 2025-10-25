# Frontend - Next.js Microservice

## Overview
This is a Next.js frontend for testing automated building, testing, and deployment processes.

## Project Structure
```
frontend/
├── src/
│   ├── pages/
│   │   ├── index.tsx       # Home page
│   │   ├── users.tsx       # Users management page
│   │   └── products.tsx    # Products management page
│   ├── components/
│   │   ├── UserCard.tsx    # User card component
│   │   ├── ProductCard.tsx # Product card component
│   │   └── HealthCheck.tsx # Health check component
│   ├── services/
│   │   └── api.ts          # API client services
│   └── types/
│       └── index.ts        # TypeScript type definitions
├── __tests__/              # Test files
├── public/                 # Static files
├── package.json            # Dependencies
├── next.config.js          # Next.js configuration
├── tsconfig.json           # TypeScript configuration
└── jest.config.js          # Jest testing configuration
```

## Installation

### Prerequisites
- Node.js 18+
- npm or yarn
- Docker (optional)

### Setup
1. Install dependencies:
   ```bash
   npm install
   ```

2. Create `.env.local`:
   ```bash
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

4. Open http://localhost:3000 in your browser

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm test` - Run tests
- `npm run test:watch` - Run tests in watch mode
- `npm run test:coverage` - Generate coverage report
- `npm run format` - Format code with Prettier

## Pages

- `/` - Home page with dashboard
- `/users` - Users management page
- `/products` - Products management page

## API Integration

The frontend communicates with the FastAPI backend at `http://localhost:8000`.

### API Services (`src/services/api.ts`)
- `usersApi.list()` - Get all users
- `usersApi.get(id)` - Get specific user
- `usersApi.create(user)` - Create user
- `usersApi.update(id, user)` - Update user
- `usersApi.delete(id)` - Delete user
- `productsApi.list()` - Get all products
- `productsApi.get(id)` - Get specific product
- `productsApi.create(product)` - Create product
- `productsApi.update(id, product)` - Update product
- `productsApi.delete(id)` - Delete product

## Testing

### Run all tests
```bash
npm test
```

### Run tests in watch mode
```bash
npm run test:watch
```

### Generate coverage report
```bash
npm run test:coverage
```

## Docker

### Build image
```bash
docker build -t nextjs-frontend:latest .
```

### Run container
```bash
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://backend:8000 nextjs-frontend:latest
```

## Environment Variables
Create a `.env.local` file for development:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Code Style
- Uses Tailwind CSS for styling
- TypeScript for type safety
- ESLint for code linting
- Prettier for code formatting

## CI/CD Integration
This project is ready for CI/CD pipelines:
- GitHub Actions
- GitLab CI
- Jenkins
- Azure DevOps

## Features
- ✅ Server-side rendering with Next.js
- ✅ TypeScript support
- ✅ Tailwind CSS styling
- ✅ API client with axios
- ✅ Unit testing with Jest
- ✅ Health check integration
- ✅ Responsive design
- ✅ Docker support
