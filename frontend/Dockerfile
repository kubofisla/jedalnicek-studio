FROM node:20
WORKDIR /frontend
COPY package*.json /frontend/
RUN npm install
EXPOSE 3000
ADD . /frontend/
CMD ["npm", "run", "dev"]
