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

## Frequency Division Multiplexing vs Time Division Multiplexing

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



