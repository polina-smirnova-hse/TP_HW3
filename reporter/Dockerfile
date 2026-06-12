FROM node:20-alpine
RUN npm install
COPY package.json /package.json
COPY report.js /report.js
ENTRYPOINT ["node", "/report.js"]
