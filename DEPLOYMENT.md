# Deployment Guide for MealPlanPro

This guide covers how to build and deploy the MealPlanPro (Frontend) application.

## 🏗 Build Process

Before deploying, you must build the application for production. This compiles the TypeScript code and optimizes the assets.

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Create a Production Build**
   ```bash
   npm run build
   ```
   *This typically creates a `build` or `dist` folder containing the static files.*

## ☁️ Deployment Options

### Option 1: Vercel (Recommended)
Vercel is the easiest way to deploy React applications.

1. **Push your code to GitHub**, GitLab, or Bitbucket.
2. Log in to [Vercel](https://vercel.com) and click **"Add New Project"**.
3. Import your repository.
4. **Configuration**:
   * **Framework Preset**: Create React App (or Vite, depending on your build tool).
   * **Build Command**: `npm run build`
   * **Output Directory**: `build` (or `dist` if using Vite).
5. **Environment Variables**:
   If you have a deployed backend, add the environment variable:
   * Key: `REACT_APP_API_URL`
   * Value: `https://your-backend-api.com`
6. Click **Deploy**.

### Option 2: Netlify
1. Log in to [Netlify](https://www.netlify.com).
2. Drag and drop your `build` folder to the dashboard **OR** connect your Git repository.
3. If connecting Git:
   * **Build command**: `npm run build`
   * **Publish directory**: `build`
4. To configure the backend URL, go to **Site Settings > Build & Deploy > Environment** and add `REACT_APP_API_URL`.

### Option 3: Docker (Container)
You can serve the static frontend using Nginx within a Docker container.

Create a `Dockerfile` in the root:

```dockerfile
# Stage 1: Build
FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
# Copy custom nginx config if needed to handle client-side routing
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🔌 Backend Configuration

This application is designed to communicate with a backend API.

1. **If you have a Backend:**
   Ensure you set the `REACT_APP_API_URL` environment variable during deployment to point to your live backend server (e.g., `https://api.mealplanpro.com`).

2. **If you DO NOT have a Backend:**
   You can still deploy the frontend! The application includes a **Test Mode**.
   * If the app cannot connect to the API (or if no URL is provided), it will fallback to internal mock data.
   * Users will see a yellow banner: *"Testing Mode: Backend not connected."*
   * **Note:** In this mode, changes (like saving recipes) will **not persist** after a page refresh.

## ⚠️ Client-Side Routing Note
This application uses `HashRouter` (`/#/planner`), which is compatible with all static hosting providers (GitHub Pages, S3, standard Nginx) without needing complex server-side rewrite rules.
