# the-russian-roulette

## Write-up

- We have the condition that takes us into the flag, so making both parts evaluated as true will get us into the flag
```js
    if (users[id] && isAdmin[user]) {
        return res.redirect("/?flag=" + encodeURIComponent(FLAG));
    }
```
- For the first condition we have a local array of users, so to make this part returns `true` we must pass a valid index that successfuly returns an existant user from it, for example `id=1`, this will return the user in the second place and will cause it to be true.
    - To have the value 1 'for example' in the variable `id` and since it's returned from the SQL query sent to the SQLLite DB using the line `const id = db.prepare(query).get()?.id;`,
    - A SQLI will be sufficient to make it pass by using this payload `' UNION SELECT 1 --`, the query will look like this `SELECT id FROM users WHERE username = 'myuser' AND password = '' UNION SELECT 1 --';` causing id to have the value `1` and gets a valid user.

- For the second part, we have an object called `isAdmin` that takes a random user alongside the russian roulette function called `makeAdmin` which turns a random user into an admin.
    - Since it's kinda impossible to get the exact user and since the `user` value is coming from the `req.body` we can basically put anything in place.
    - In javascript there are default methods that exists in any object created, as a result if we passed any of the default methods such as `hasOwnProperty | valueOf | toString | propertyIsEnumerable | isPrototypeOf | constructor and so on...`, this will result the condition to be true as we're returning a valid function that turns into a true value in a conditional evaluation.

- Both conditions are true, we got the flag and yes, we're the russian roulette masters!

## Flag

`shellmates{yOu_4rE_tHE_RUS$IaN_r0Ul3Tte_M4sTEr}`