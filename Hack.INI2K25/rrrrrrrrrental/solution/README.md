# rrrrrrrrrental

## Write-up

By checking the code source we will find out that our js script is registering a service worker that is located on `/sw.js`, by checking the sw code we will find that it's obfuscated, after deobfuscating it we will find that it is checking on each request if in the request url we're getting the `features.json` file (which contains the flag), if the string is present it will change the request to be `faeture.json` which is the fake flag. Notice also that the server has protection mechanism that checks if the all the car pages are visited before allowing to access the flag, so we need to visit all the pages first.

- We have actually two options to get the flag whether a browser oriented solution where we need to modify the service worker code to return the flag without checking for the string and that's by checking the browser settings and modifying the service worker code using the inspect tool, after that we can just refresh the page and get the flag, we can also unregister the service worker it will work also!

- The second way is to not use the browser at all, we can just use curl to pass by all the pages to bypass the session all pages visited check and then get the flag directly, the [exploit.py](./exploit.py) file contains the details!

## Flag

`shellmates{sw_c4ch3_c0n7r0ll3d_7h3_7ru7h}`