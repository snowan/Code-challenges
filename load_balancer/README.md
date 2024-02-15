## Load balancer

[build a Load Balancer](https://codingchallenges.fyi/challenges/challenge-load-balancer)

This task is to build a L7 application load balancer -- which will route HTTP requests from clients to a pool of HTTP servers.

This project is to build a load balancer that meets:
- LB can send traffic to two or more servers
- health check the servers
- Handle a server going offline (failing a health check)
- Handle a server coming back online (passing a health check)

### Step 1
1. start terminal and backend_server `python3 backend_server.py` 
```
python3 load_balancer/backend_server.py            
Backend Server is listening on ('localhost', 8081)
```
2. start another terminal and load_balancer `python3 load_balancer.py`
```
python3 load_balancer/load_balancer.py
Load Balancer is listening on ('localhost', 8080)
```
3. start third terminal, and curl 
```
curl http://localhost:8080 --output -
Hello From Backend Server%                   
```

```
# output from backend server  
Replied with a hello message
Received request from ('127.0.0.1', 58729)
GET / HTTP/1.1
Host: localhost:8080
User-Agent: curl/8.1.2
Accept: */*

Replied with a hello message

# output from load balancer
Hello From Backend Server
Received request from ('127.0.0.1', 58728)
GET / HTTP/1.1
Host: localhost:8080
User-Agent: curl/8.1.2
Accept: */*

Response from server: HTTP/1.1 200 OK

Hello From Backend Server
```

### Step 2 Round Robin 
1. start a terminal and server 1 
```
python3 load_balancer/backend_server_5001.py
 * Serving Flask app 'backend_server_5001'
```
2. start a new terminal and server 2
```
python3 load_balancer/backend_server_5002.py
 * Serving Flask app 'backend_server_5002'
```
3. start a new terminal and load balancer
```
python3 load_balancer/round_robin_lb.py
Load Balancer is listening on ('localhost', 8082)
```
4. test round robin 
```
# curl from 8082 multiple times and monitor lb output
curl http://localhost:8082/ --output -

# output from lb, requests hit server 1 and server2 round robin
python3 load_balancer/round_robin_lb.py
Load Balancer is listening on ('localhost', 8082)
Received request from ('127.0.0.1', 60753)
GET / HTTP/1.1
Host: localhost:8082
User-Agent: curl/8.1.2
Accept: */*

Response from server: Hello from Backend Server 5001!
Received request from ('127.0.0.1', 60777)
GET / HTTP/1.1
Host: localhost:8082
User-Agent: curl/8.1.2
Accept: */*

Response from server: Hello from Backend Server 5002!
Received request from ('127.0.0.1', 60831)
GET / HTTP/1.1
Host: localhost:8082
User-Agent: curl/8.1.2
Accept: */*

Response from server: Hello from Backend Server 5001!
Received request from ('127.0.0.1', 60835)
GET / HTTP/1.1
Host: localhost:8082
User-Agent: curl/8.1.2
Accept: */*


Response from server: Hello from Backend Server 5002!
```

### Step 3: add health check 
Similar as step 2 

output from lb
```
Response from server: Hello from Backend Server 5002!
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is healthy.
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is healthy.
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is healthy.
Performing health check...
```
- modify server health return code and message, you can get unhealth status, and it will not route to unhealth server when make requests
```
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is unhealthy (status code: 500).
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is unhealthy (status code: 500).
Performing health check...
Server ('localhost', 5001) is healthy.
Server ('localhost', 5002) is healthy.
Server ('localhost', 5003) is unhealthy (status code: 500).
```

- run parallel with `curl http://localhost:8085/ & curl http://localhost:8085/ & curl http://localhost:8085/ &`
```
Response from server: Hello from Backend Server 5003!

Response from server: Hello from Backend Server 5001!

Response from server: Hello from Backend Server 5002!
```