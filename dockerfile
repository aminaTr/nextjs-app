# Use the official Node.js image.
FROM node:20.17.0

# Set the working directory in the container.
WORKDIR /app

# Copy package.json and package-lock.json files.
COPY package*.json ./

# Install dependencies.
RUN npm install

# Copy the rest of your application code.
COPY . .

# Build your Next.js application.
RUN npm run build

# Expose the port the app runs on.
EXPOSE 3000

# Command to run your application.
CMD ["npm", "start"]
