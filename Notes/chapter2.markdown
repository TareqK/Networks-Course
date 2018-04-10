# Chapter 2 : Application Layer

In this chapter, we will be looking at the 5th(and highest) layer of the
TCP/IP stack. This is called the **Application Layer**.

But what is an Application from a network POV?

Some example of network apps are email, web, text messaging, VoIP, 
video streaming, etc. We wont be talking about them all, we will be talking 
about the more common ones. 

---

## Creating Network Applications

we need to :

1. Run on different end systems.
2. Communicate over network.

we don't need to : 

1. Write for network core devices
2. Write end-system applications

---

## Structures of Applications 

1. Client-Server Applications : 
   has 2 parts The server, which is always on, has a permanent ip address, 
   and is usually in a data center, for scaling. and the client, which communicates with
   the server, and not directly to its peers.
   
2. Peer-to-Peer Applications : 
   Have no server, the peers(the end systems) talk directly to each other.
   It is self scaling, since each peer added to the network carries its weight. 
   It is more complex to manage.

---

## Process Communication

Within the same host, two processes communicate using inter-process communicaton, 
defined by the OS. However, between hosts, they talk by exchanging messages.

The Client process is the one that initiates the process, while the server is the
one that is waiting to be contacted.

---

## Addressing Process 
It is not enough for an IP address to identify a process. For this we have
2 things added to the IP address which are : Sockets and Ports.

---

### Sockets and Ports

A socket is the the path between application and transport. It is analogous
to a door, which allows two way communication. Sockets are opened to allow
communication. Port numbers tell us which application we are sending the 
data to. We have 2^16 ports available. Some common port numbers are
80,25,20,21,22,23,53,etc each of which are have an application associated to them. 
In fact, the first 1000 ports are reserved ports. ICANN is the body that 
handles port reserving.

Data is always sent sequentially. This means that sockets are released 
when they are not in use.

---

The Application layer defines :

1. Types of message
2. Message Syntax
3. Semantics
4. Rules

## Data Integrity and Transport Protocols

Some apps need 100% data integrity. Others can tolerate some loss. 

Some applications are interactive, real time applications. Others are
not.

We also need to consider security and throughput(constant or plastic vs
varying or elastic ).

We need to chose the appropriate transport protocol for our application.

There are 2 main services:

1. TCP : reliable, flow control, congestion control, but slower, and 
needs setup(connection oriented).

2. UDP : Unreliable, no control, no security, no connection.

However, UDP is significantly faster than TCP, but TCP is safer. 
each of them has a use in network applications.

VoIP, live streaming, and games use UDP. Web applications, email, and
text messages use TCP. 

---

## Web and HTTP 

a web page consists of objects connected to each other Connected by a 
base HTML file(index). Each objects is addressable by a URL.

HTTP stands for **H**yper **T**ext **T**Ransfer **P**rotocol, which 
is on port **80**. It used TCP. It is a stateless protocol, that is it 
does not have a sessions. This is because protocols with states are 
complex. 


There are 2 types of HTTP : 

1.Non-Persistent HTTP, where  one object is moved through the TCP socket, 
the socket is closed, and then another(or the same) socket
is opened for the next.

2.Persistent HTTP, which keeps the socket open and 
sends multiple objects between the client and server. This is known as
HTTP keep-alive. The number of objects transferred in one connection 
depends on the traffic of the server.

The default type is Persistent HTTP. However, sometimes we might want to 
use non-Persistent HTTP. This might happen if there is a lot of traffic,
and we want to serve all these clients, and the time period for each 
client will only allow us transfer 1 object. This rarely happens, but
it is always good to be prepared.

The time of persistent HTTP is better. This is because we need to 
open less sockets, therefore, we dont need to handshake as often, 
which means the **round trip time** is not repeated as often,
only the **transmission time** is added up after the socket is opened.

In fact, response time is given by :

> response time = 2\*round trip time + transmission time 

There are 2 types of HTTP messages :

1. Request : This is a human readable ASCII message that asks the server
for a certain object. There are multiple types of request(GET, POST, PUT, DELETE).

2. Response :  This is the response to our HTTP request. It contains a header, 
about what the data type is, the status code, and the data. It also contains
a bunch of other things, but these are the most important parts usually.

---

### User-server state : Cookies

A Cookie is a small piece of information that the server writes on the 
client for later use. The cookie is in the header of the HTTP response,
and is sent with every new request to the website, also in the header.

Even though HTTP is a **stateless** protocol, using cookies, we can keep
authorisation and authentication across a website, and even sometimes
across websites.

Cookies are used for authorisation, shopping carts, recommendation, 
user session states, etc. They do however permit sites to learn a 
lot about you, and are a privacy concern.

---

### Web Caches and Proxy Server

The goal of a proxy is to satisfy client requests without involving
the origin server. This means that we reduce the congestion 
on the bandwidth line, with the added benefit of security and 
filtration. 

The proxy can cache some objects, and when they are requested, it
gets the differentials from the origin server.

Proxies are outside facing. This is because it makes no sense to 
cache a local server. 

This is all done through the **Conditional GET Request**. It specifies
an if relating to if the content has been modified, and if so, fetches
the differentials.

---

## Electronic Mail : SMTP, POP3, IMAP

Email has 3 components :

1. User Agent 
2. Mail Servers
3. Simple Mail Transfer Protocol

Email is a reliable transfer protocol, using port numbers 25 and 100.
SMTP is a push protocol. An email message has 2 parts : a header, containing
from, to, subject, CC, BCC, etc, and the body, which is an ASCII message.

Attachments are sent along with the mail, and are part of the message.

---

## DNS : Domain Name Service

DNS is a distributed database of IP addresses and domain names(it
is a bit more convoluted, but lets assume it is like that). The purpose 
of DNS is to give internet locations(servers) a human-readable name 
that can be translated into a computer-readable one. For example, 
www.mydomain.com references some IP address 192.172.142.134 . 

This makes it easier to remember websites and other resources on a network.
Instead of putting all these IP addresses, we just have to remember
its **URL**.


This database is distributed over many many servers. 

The Workflow is as follows :

- The application sends the domain name we want to the DNS server.

- The DNS server looks up the domain name and finds its IP.

- If it is not on the DNS server, the DNS server looks for it on another
DNS server, then caches it.

- The DNS server returns the IP address.

There are different kinds of DNS Servers

- Top Level Domain : these are responsible for a whole domain, such as .com, .org, etc.

- Authoritative : these are DNS servers that belong to an organisation. These are the only
DNS servers that can give us an IP address(except for local cache).

- Local DNS server : does not really belong to a hierarchy, for example, each ISP has one.

### Iterated Queries 

(I dunno, go talk to that server)

- I send the query to the local(default) DNS.

- Its not there, so the DNS server returns the IP address of the DNS server
that has it.

- If it is not there, the DNS server returns the IP address of the DNS server
that has it, and so on and so forth, until it is found.

- Once it is found, the local DNS returns the IP address to me.

---

### Recursive Queries 

(hold on ill go grab it for you)

- I send the query to the local DNS.

- If it is not there, the local DNS sends it to a higher level DNS.

- If its not there, it sends it to an even higher level DNS.

- This keeps going on until the IP is found, and is returned through
all the servers on the path.

- Once it is found, the local DNS returns the IP address to me.

---

Iterative is faster than recursive, however, there is a higher load
on the local(default) DNS.

Queries are done over UDP, Resource Records are transferred using TCP.

### DNS records 

Distributed DB storing Resource Records.

Resource Record format : (name, value,type, ttl).

Types :

- Type A  : name is hostname, value is IP.

- Type NS : name is domain(foo.bar), value is the hostname of the authoritative name server of the domain.

- Type CNAME : name is alias for some real(canonical) name, value is canonical name.

- Type MX : value is the name of the mailserver associated with the name.

Each new registration will create  a type A record for the site, and a 
type NS record for the domain. If we went to register a mail server we also 
need a type MX record. If our organisation has multiple servers for the 
same service(eg local servers in each region for the website), we also 
need type CNAME record. We register at a DNS registar.

---

### DNS Query/Response Structure

A DNS query and response have the same structure, which looks like this :

![DNS  Query/Response structure](https://upload.wikimedia.org/wikipedia/commons/4/40/Dns_message.jpg)

---

### Attacks on DNS

- DDOS.

- Redirect.

- Bombard TLD.

- Exploits. 

---

### Caching 

DNS servers will cache the responses that they get if they dont already
have them. This makes it faster, because we dont have to go through
the whole process. Your local DNS especially does this.

---

## Peer to Peer Architecture

Peer to Peer architecture is a network architecture that differs from 
client/server, in that the client is also the server, and each peer in 
the network has part of the content, and provides resources to other 
peers.

There is a lot of controversy surrounding peer to peer, because a lot 
of applications violate copyright laws. However, peer to peer is faster,
and infinitely scalable, since each new peer adds resources and load to 
the system.

In peer to peer, peers are any device on the network. Information 
is transmitted between these devices without the need for a server. 
Because of this structure, peer to peer allows us faster transfer speeds,
because we take the data from multiple places at the same time. 

### File Distribution

In client/server architecture, the server distributes a file to 
multiple clients. There a bunch of limits here : the upload capacity of the 
server, the download capacity of the client, and the upload capacity 
of the client. Furthermore, the file transfer goes at the rate of the
**slowest client download**. This causes a higher distribution time.

However, in peer to peer, every client is also the server, and each 
file is split into multiple parts spread across multiple clients, 
resulting in higher overall throughput and utilization. Further more, 
the server(or the first seeder) needs to only send the file once, 
and the peers then distribute it to each other. 

The speed of peer to peer and client/server models have equations
to calculate them, look these up yourself.

#### BitTorrent

BitTorrent is an example of a peer to peer file transfer service.

The BitTorrent network has 2 parts : the tracker, which tracks the peers
participating(and what chunks they have of the file),
and the torrent, the group of users exchanging chunks of a file.
Files are divided into 256Kb chunks(usually), and peers in the torrent
send/receive file chunks.

To Join a torrent, we register ourselves on the tracker that is tracking
this torrent. Upon joining the torrent, the tracker sends the list of peers to the new
peer(and adds it to the peer list). Once the peer is in the torrent,
it starts gathering chunks of the file(and uploads the chunks it has),
until it is complete. After that,it can either leave the network,
or it can stay on the network and upload chunks to other peers. 

It is a bit more convoluted, since requests, responses, and which 
chunks are transferred are all determined by a special algorithm. But the
basic idea remains.

---

### Scalability 

Peer to peer networks are infinitely self scalable, due to the fact that each
peer adds resources and load, and its total bandwidth keeps increasing as well.

Eventually, the time needed to transfer a file reaches a limit, since there
is more than enough bandwidth.

---

##  Content Distribution Networks

Special Topic Read up.

## TCP and UDP

Read up.
---
