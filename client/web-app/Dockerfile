FROM node:16.13-slim
# FROM node:8.7.0-alpine

ARG WEB_APP_HOME=/webapp

WORKDIR ${WEB_APP_HOME}

# Packages are installed here to ensure they will be cached.
COPY ./package.json ./

# COPY ./package-lock.json ./

RUN npm install

RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

COPY . .

CMD ["npm", "start"]