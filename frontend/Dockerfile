FROM node:14
WORKDIR /frontend
COPY package*.json /frontend/
RUN npm install
EXPOSE 3000
ADD . /frontend/
CMD ["npm", "start"]