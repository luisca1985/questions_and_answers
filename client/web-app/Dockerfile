FROM node:16.13-slim

ARG WEB_APP_HOME=/webapp

WORKDIR ${WEB_APP_HOME}

# Packages are installed here to ensure they will be cached.
COPY ./package.json ./

COPY ./package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]