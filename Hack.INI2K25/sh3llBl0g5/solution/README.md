# sh3llBl0g5

## Write-up

Vue.js leaked source map which contains the credentails of the firebase database config, the user can access the database and read the blog posts by using the firepwn tool, we will find the flag in a collection called `bG9ncw` where the flag is one of the documents, the idea is that this collection is hidden and only after reading the source map deeply.

## Flag

`shellmates{f1r3$70r3_rul35_m15c0nf1gur4t10n5_g035_brrrrrrr}`