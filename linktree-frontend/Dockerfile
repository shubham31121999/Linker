# Use Node.js image for building Vite app
FROM node:20-alpine

WORKDIR /frontend

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

# Start Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
