import random

ran = random.randrange(10**80)
myhex = "%064x" % ran

adds = "0x" + myhex[:40]
print(adds)
