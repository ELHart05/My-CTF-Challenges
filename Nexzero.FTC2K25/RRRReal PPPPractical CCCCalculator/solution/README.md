# Challenge name
RRRReal-PPPPractical-CCCCalculator

## Write-up

By taking a look at the challenge title we can know that it's something related to RPC logic and protocol, speaking of RPC we cannot forgot to mention the NFS, we know that RPC is a communication protocole that runs between a client and a server, the server has procédures to execute and the client have the IDs/name of those procédures, as a result the client just need to call the server remotly by sending the number/name of the procedure and the arguments needed and he will get the output requested, in this case we need `the name of the method to call so we can read the flag file`

We need three things to achieve that,
- The host and the port that's running the rpc server,
- The name of the method to call so we can read the flag file or execute commands or something...
- At least one of the The RPC pb2 generated files upon creating the proto file to list all the methods needed.
And then we can build a python script that connects to the server and have access to the methods listed and we can execute any method.

If we use Nmap tool to scan the ports using `nmap @IP` we can find the TCP port that the server uses, it's always 8888 in this case, upon checking the ports we will encounter the NFS port also open which means there's a possibility of remotly access a certain file we can mount the remote folder by using `sudo mount.nfs4 -v @IP:/ /mydirectory` we will find the `calculator_pb2.py` by reading it we will find the `DESCRIPTOR` of the proto file, it's a bit mixy since the methods names are written in a coded version with the descriptor in the file but it can be extracted, by using the `DESCRIPTOR` we need to reverse generate the .proto file and then compile it using `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto`, generate the original two grpc files and create a py script that call the x9 method which will read the flag, all good!

## Flag

`nexus{444444444444444hhhhhh_rpc_53rv3r_3xp053d}`
