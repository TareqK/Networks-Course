# Chapter 1 : Introduction

## What are Computer Networks?

A computer network is a set of devices connected to each other. In it's 
simplest form, it is 2 computers connected to each other. There are many
ways to connect computers, wired(ethernet, coax, fiber) and wireless(mobile networks,
IR, Microwave, Bluetooth). We also need a protocol to communicate between the devices

--- 


## What is the Internet?

The internet is a huge network of networks. Throughout this course, we will
be looking at it as a case study in many cases.

### Internet Structure 

- End systems connect to the internet via **access ISPs**.
- Access ISPs connected to each other.
- Resulting complex are very complex. 

![internet structure](http://imada.sdu.dk/~jamik/dm543-14/material/Week1/network-of-networks.png)

As we can see from above, ISPs connect to other ISPs and to higher tier ISPs. The 
data travels between them until  it reaches the place it is supposed to.

Tier 1 ISPs are the highest level of ISPs that talk to each other.(eg Paltel, Sprint, AT\&T)

Tier 2 ISPs are the second level.(Hadara, Mada, CallU, other regional ISPs)

Tier 3 ISPs are institutions.(Birzeit, Polytech)

Tier 4 ISPs are local area networks.(you home)

IXPs are a central point for ISPs to connect to.

Content providers provide the content(web pages, videos, pictures, etc).

---

## Packet Switching and Circuit Switching

Say i have 2 machines that want to talk to each other, one wherever i am 
and one in Canada. There are 2 ways they can talk : circuit switching and
packet switching.

### Circuit Switching

1. Setup connection.
2. Reserve bandwidth/resources until you release them.
3. All data moves in the same route(1 path) in order.
4. Quality of Service is (almost) guaranteed.
5. More secure.
6. Works on Circuit Switching IDs.
7. More expensive.
8. Can be blocked if there aren't any lines available(less capacity).

--- 

### Packet Switching

1. No Connection Setup.
2. Shared Bandwidth.
3. Multiple routing(multiple paths), data might move out of order.
4. Quality of Service is best effort(not guaranteed).
5. Less Secure.
6. Works on Destination ID's.
7. Less expensive.
8. Can't be blocked, put can get slow.

---

Telephony works on circuit switching. The Internet works on packet switching.
However, some institutions like ministries and military institutions, can have
internet over circuit switching, or through a hybrid approach.

Packet switching, because it divides the data to packets and sends them through
multiple paths, It allows more users to use the network(theoretically infinite
users), however, it has a higher latency and data takes longer to transmit.


---

### Frequency Division Multiplexing vs Time Division Multiplexing

FDM means that we divide the bandwidth into a set of frequency channels.
an example of this is FM radios. They all have the same bandwidth, at 
a different frequency, for as long as they want. However, the bandwidth 
reserved may not be utilised. The internet does not work like this, because
there is a lot of unused bandwidth, and the internet needs every drop.

TDM means that we give each user a time slot on the bandwidth, where they
have the whole bandwidth for a small period of time.  They all get the 
whole bandwidth, but not forever. This causes a delay, but this is a 
trade-off so we have more utilisation of the bandwidth. The internet
works like this.

There are other means of multiplexing, but these are the main 2 kinds we 
will look at. 
  
---

## Delay, Loss, and Throughput



### Loss

Packets are usually transmitted and queued on the receiving end until 
the message is complete. Sometimes, some packets to not arrive, so they 
have to be re-requested. This is called **loss**. It is caused becuase 
of the way that packets are transmitted, where they are queued on the 
receiving end. 
 
---

### Delay 

There are many sources of delay. It could be caused by the connection
to your ISP being overloaded, your switch/access point being crowded.
This is called **transmission delay**.  This is the usually the source
of delay, and usually the biggest one. This is expressed by

> L<sub>a</sub>/R 

where L<sub>a</sub> is the size of the data and R is the bandwidth.

Close to 0, there is no delay. If it is close to 1 , it gets slower. A 
ratio of higher than 1 means there are losses.

Another source of delay is **nodal processing**. This is caused by one 
of the devices(server or client) not having the resources to handle 
the amount of requests/responses. This is rarely the source of delay

**Propagation delay** is delay caused by the distance between the server
and the client. It is worse for wireless mediums than for wired ones. This
has the smallest effect on delay.

The fourth source of delay is the **queuing delay**. This is caused by
the buffer being filled, causing losses if it has to clear buffers. This
may occasionally happen, but is not often the source of delay.

---


### Throughput

Throughput is the rate(bits/unit time) at which bits transferred between the sender
and receiver. There are 2 kinds :

1. Average Throughput : The Throughput over a long period of time.
2. Instantaneous Throughput : The Throughput at a certain instant of time.

The rate is dependant on the bandwidth. This is
called the **bottleneck**. The bottleneck link is the link on the end to end path 
that constraints an end to end throughput. Usually, the client has a lower bandwidth.
However there are some cases, when there is a lot of load(or traffic) on the server, 
that the bottleneck is coming from the server.

## Layers and Protocols

Networks have many pieces and components. They are very complex
and interdependent. 

Transferring data over the network takes a series of steps, each of which
is responsible for a part of the transmission. This makes it easier to 
trace errors and keep things in check. Traditional networking has 5 layers
(more modern networking models have 7 layers).

The Layer model has its pros and cons. It makes it easier to manage a complex system
and keep it's components updatable and maintainable. However, Layering makes it
difficult to improve a complex system, because the whole system has to be 
improved.

Here are the 2 models, side by side :

![layers](https://www.tutorialspoint.com/ipv4/images/tcpip_layers.jpg)


Throughout this course, we will be discussing the TCP/IP reference model. 
Each layer has its own role, and we will be talking about each in detail.

### Encapsulation

Every message sent on the TCP/IP stack has some identifiers attached to it.

![encap](https://flylib.com/books/4/271/1/html/2/files/02fig02.gif)






