# Chapter 3 : Transport Layer

There are 2 protocols in the transport layer, UDP, which is a best effort
protocol, and TCP, which is a reliable data transfer protocol.

## UDP 

UDP is connectionless, ie, no handshaking. In UDP, each segment is sent
and handled independently of others. UDP has many uses, such as DNS, 
streaming, and SNMP.

Data in UDP can sometimes not arrive or arrive out of order or arrive jumbled.

### UDP Segment Header 

![header](data:image/jpeg;base64,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)

The checksum is a value that is calculated from the data on the sending
and receiving side and tells us if the data arrived correctly or not. If it
is correct, the data is raised to the application layer, otherwise, it is 
ignored. There is no re-requesting.

This header is sent with every datagram. 

---

## Reliable Data Transfer

Reliable data transfer means that the data is guaranteed to reach the 
target(eventually), without any missing parts, and correctly. All media 
we use in transporting data (ethernet, wifi, cable, etc) are all unreliable channels. 
Therefore, we need a protocol to handle reliable data transfer. This is called
a reliable data transfer protocol(rdt) between the 2 end machines.


### RDT 1.0 

Reliable transfer over a reliable channel.  This is not realistic. This
protocol does not exist.

### RDT 2.0

Channel may flip bits in packet, ie, errors, not losses. How do we recover 
from these errors?

In this case, we need **acknowledgements**. There are 2 acknowledgements, 
positive(ACK) and negative(NACK). If a positive acknowledge is sent, then the data
has arrived correctly. If a negative acknowledgement is sent, then the 
data has not arrived correctly and needs to be resent.

However, lets say that we sent an ACK, but it arrived as a NACK, and the 
data is resent, and the receiver gets it and adds it to the queue. We now
have duplicate data, which is a problem.

RDT 2.0 added 2 new mechanisms, error detection, and feedback as control messages.

RDT 2.0 i a stop and wait protocol. The next packet is not sent until the current
one is acknowledged. This is achieved by adding a sequence number to each packet, 
flipping between 1 and 0 between packets. The receiver expects that a 1 will be followed 
by a 0, if that does not happen, or the wrong number in the sequence arrives, it 
re-requests it.

However,a  problem arises if we send a NACK and it becomes an ACK along the line, resulting
in missing or jumbled chunks.

This is solved by removing the concept of NACK, and sending an ACK along with  a 
sequence number (0 or 1).

However, if the 1 or 0 sent with the ACK were flipped along the way, then 
we confirm wrong data, and our data ends up missing.

Some missing stuff from slides about RDT 2.1 and RDT 2.2



### RDT 3.0


Here we assume we can have losses and errors. 

Here we introduce timeouts. If after a certain time the acknowledgement is
not received by the sender, so it is sent again, the sender waits again, 
and does this until ACK comes through.

However, What if the ACK gets lost? in that case, the sender sends the 
packet again after the timeout, and waits for the ACK. 

But what if the ACK arrives after the time out? in that case, the 
sender resends the packet, and when the ACK arrives, sends the next packet,
and the receiver deletes any duplicates.


### Pipelining

Pipelining has the sender send multiple packets and wait for multiple 
acknowledgements, allowing more utilization. There are 2 generic forms
of pipelined protocols, **go-Back-N**, and **selective repeat**.

#### Go-Back-N

- Sender can have up to N unacked(a window) packets in pipeline. Receiver only sends
cumulative ack. Sending an ack at packet 5 means that all of the 5 packets 
have arrived successful. If a packet has not arrived, the last ack sent is the 
ack of the highest inorder sequence.

- Sender has a timer for the oldest unacked packet. When this timer expires, 
resend all the unacked packets.

- The Sender will always send N packets, regardless of what has been acked. If we ack 
1, then the sender will send packets 2-6 so it sends 5 packets.

However GBN is wasteful, since it dumps a lot of data.

#### Selective Repeat

- Receiver individually acks all correctly received packets. They are buffered as needed,
until they all arrive and are in-order. 

- Sender only resends packets for which ack is not received.

- Sender has a window of N consecutive sequence numbers, and a limit on the 
sequence number on windows.

- The window moves forward with every ack on a lower-level  packet.

However, there are cases where sequences overlap.

TCP solves these issues by combining the cumulative ack from GBN and the buffer from SR. However, 
it acks the next expected sequence number to the highest in order sequence. This results in the ack 
telling us which  packet we are missing, not the ones we have. Furthermore, it doesnt use sequences, 
it uses byte positions instead. Acking byte 11 means that we want the sender to resend byte 11-40(assuming a window 
of 30 bytes).

### RDT 4.0

Missing

---

## TCP

1. Point to point, one sender, one receiver.

2. Reliable in order byte stream.

3. Pipelined.

4. Full Duplex.

5. Connection Oriented.

6. Flow control.

### Round Trip Time

How do we set the Round Trip Time? If its too short, we could retransmit 
too often(or forever). If it is too long, we have slow reaction to segment loss.

The best we can do is estimate it, and measure it and work with that. 

We use a SampleRTT, which is the time from segment transmitting to ack receipt, 
ignoring retransmitting. SampleRTT will vary, so we need several recent measurements
and the average of them, resulting in the estimated round trip time, EstimatedRTT

The equation is given by 

> EstimatedRTT = \(1 - &alpha;\) \* EstimatedRTT + &alpha; \* SampleRTT

and 

> Timeout = EstimatedRTT + 4\* DevRTT

where DevRTT is the standard deviation from RTT. 4\*DevRTT is known as
the **safety margin**.

DevRTT is guven by 

> \(1 - &beta;\) \* DevRTT + &beta; \* \| SampleRTT - EstimatedRTT \|


### TCP Actions

Look up the table in slides

### TCP Fast Retransmit

If we get a duplicate Ack for a segment 3 times in a row(ie, 4 total Acks for 
that segment), then the packet is 
instantly retransmitted. Why 3? Because testing showed that this is good
enough. Therefore, we save what is left of the timeout time. Less causes
overhead, more causes time delays.

### Flow Control 

TCP allows for flow control. It allows us to control the amount of data
sent to  the receiving end. ie, the Receiver Controls the sender, so 
the sender wont overflow the receivers buffer with data. 

The Receiver sends the amount left free in the buffer to the sender 
with the packets. The Sender then limits the amount of in-flight packets 
to this amount, to guarantee that the buffer doesnt overflow.


### Connection Management

TCP has a connection setup, and similarly, a connection close.

TCP uses a 3-way handshake to start the transfer. We use a 3 way handshake
instead of a 3 ways handshake so we dont end up with half-open connections. 
These are connections made but forgotten about and left open.

Furthermore, the 3-way handshake ensures that the segment and 
sequence numbers are in sync.

Similarly, TCP uses a 3-way FIN(technically 4, but we use **piggy banking**, 
ie, to send more than one command in a single segment, to reduce the number of steps
) to close the connection, and the connection is 
closed at the client and the server, so we dont have half-closed connections,
that are connections that are still open on one side and useless. 

Of course, while the client requests the closure(in a normal case), 
the server is the one whose connection is terminated first.

There are cases when the server initiates the closure. For example, in 
non-persistent HTTP, the server sends the object and initiates closing the connection
instantly.


### Principles of Congestion Control

Congestion means too many sources sending too much data too fast 
for network to handle. It is different from flow control. It leads
to lost packets and long delays.

Congestion control is adapting our behavior to these conditions.


---


