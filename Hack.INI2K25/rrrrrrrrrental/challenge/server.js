const express = require("express");
const path = require("path");
const app = express();
const fs = require("fs");
const session = require("express-session");
require('dotenv').config();

app.use(session({
  secret: process.env.SECRET_KEY,
  resave: false,
  saveUninitialized: true
}));

const LIMIT = 50;

app.get("/static/cars.json", (req, res) => {
  const page = parseInt(req.query.page || "0");
  const limit = LIMIT;
  const cars = JSON.parse(fs.readFileSync(path.join(__dirname, "public/static/cars.json")));
  const start = page * limit;
  const end = start + limit;

  if (!req.session.pagesViewed) req.session.pagesViewed = [];
  if (!req.session.pagesViewed.includes(page)) req.session.pagesViewed.push(page);

  let toReturn = cars.slice(start, end);
  if (toReturn.length == 0) {
    toReturn = ['done']
  }
  res.json(toReturn);
});

app.get("/features/feature.json", (req, res) => {
  const cars = JSON.parse(fs.readFileSync(path.join(__dirname, "public/static/cars.json")));
  const totalPages = Math.ceil(cars.length / LIMIT);

  if (!req.session.pagesViewed || req.session.pagesViewed.length < totalPages) {
    return res.json({ status: "error", message: "You must view all cars first." });
  }

  req.session.pagesViewed = [];
  res.type("text/plain").send(fs.readFileSync(path.join(__dirname, "public/features/feature.json"), "utf8"));
});

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendStatus(200); // for kubernetes healthcheck
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`RRRRRental listening on port ${PORT}`));
