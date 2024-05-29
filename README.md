# Entropy - A Distributed Message Queue

Entropy is a side project of mine where I aim to build a distributed message queue has the below targets. The name comes from my favorite Physics concept. Entropy is also the hidden cause of most of our troubles the same way I expect the Consensus protocol to be a source of mine

- [ ] Multiple Writers can connect and write messages onto the queue
- [ ] Multiple Readers can connect and read messages from the queue
- [ ] Relative ordering of messages is maintained
- [ ] Queue has persistence either by saving the messages to a database or a file
- [ ] Queue has multiple replicas in a distributed manner to provide reliability against node deaths
- [ ] Queue uses Paxos to maintain Distribued Consensus and relative ordering across all replicas are the same