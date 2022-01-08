FROM node:16.13-slim

ARG WEB_APP_HOME=/webapp

WORKDIR ${WEB_APP_HOME}

# Packages are installed here to ensure they will be cached.
COPY ./package.json ./

# COPY ./package-lock.json ./

# RUN npm config rm proxy
# RUN npm config rm https-proxy

# RUN npm config set registry https://registry.npmjs.org/

# RUN npm config set proxy http://server:8000

# RUN npm config set https-proxy http://server:8000


RUN npm install

RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

COPY . .

EXPOSE 3000

RUN npm config set proxy http://server:8000

CMD ["npm", "start"]