FROM node 

WORKDIR /app

COPY . ./app

RUN npm i

EXPOSE 3000

CMD [ "node",'app.js' ]