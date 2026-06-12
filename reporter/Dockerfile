FROM node:20-alpine
COPY package.json /package.json
COPY report.js /report.js
RUN npm install
ENTRYPOINT ["node", "/report.js"]
