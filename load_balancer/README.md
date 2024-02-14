### Load balancer

[build a Load Balancer](https://codingchallenges.fyi/challenges/challenge-load-balancer)

This task is to build a L7 application load balancer -- which will route HTTP requests from clients to a pool of HTTP servers.

This project is to build a load balancer that meets:
- LB can send traffic to two or more servers
- health check the servers
- Handle a server going offline (failing a health check)
- Handle a server coming back online (passing a health check)

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