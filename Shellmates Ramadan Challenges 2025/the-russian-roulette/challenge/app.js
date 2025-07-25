const express = require('express');
const crypto = require('crypto');

const app = express();

const db = require('better-sqlite3')('db.sqlite3');
db.exec(`DROP TABLE IF EXISTS users;`);
db.exec(`CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);`);

const FLAG = process.env.FLAG || "shellmates{TEST_FLAG}";
const PORT = process.env.PORT || 3000;

const users = [...Array(100_000)].map(() => ({ user: `user-${crypto.randomUUID()}`, pass: crypto.randomBytes(8).toString("hex") }));
db.exec(`INSERT INTO users (id, username, password) VALUES ${users.map((u,i) => `(${i}, '${u.user}', '${u.pass}')`).join(", ")}`);

const isAdmin = {};

function makeAdmin() {
    console.log('Let the roulette spin...');
    for (const key in isAdmin) {
        delete isAdmin[key];
    }
    const newAdmin = users[Math.floor(Math.random() * users.length)];
    isAdmin[newAdmin.user] = true;
}

makeAdmin();

app.use(express.urlencoded({ extended: false }));
app.use(express.static("public"));

app.post("/api/login", (req, res) => {
    const { user, pass } = req.body;

    const query = `SELECT id FROM users WHERE username = '${user}' AND password = '${pass}';`;
    try {
        const id = db.prepare(query).get()?.id;
        if (!id) {
            makeAdmin();
            return res.redirect("/?message=Incorrect username or password");
        }

        if (users[id] && isAdmin[user]) {
            return res.redirect("/?flag=" + encodeURIComponent(FLAG));
        }

        makeAdmin();
        return res.redirect("/?message=You're not the admin, re-roll the roulette...");
    }
    catch {
        makeAdmin();
        return res.redirect("/?message=Nice try...");
    }
});

app.listen(PORT, () => console.log(`Listening on port ${PORT}`));