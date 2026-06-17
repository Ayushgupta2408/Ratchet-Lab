from alice import Alice
from bob import Bob

shared_secret = b"abcdefghijklmnopqrstuvwxyz123456"

alice = Alice(shared_secret)
bob = Bob(shared_secret)

msg1 = alice.send("Hello Bob")
print("Encrypted:", msg1)

plain1 = bob.receive(msg1)
print("Bob received:", plain1)

msg2 = alice.send("How are you?")
print("Encrypted:", msg2)

plain2 = bob.receive(msg2)
print("Bob received:", plain2)

msg3 = alice.send("Bye")
print("Encrypted:", msg3)

plain3 = bob.receive(msg3)
print("Bob received:", plain3)