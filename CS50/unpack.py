def total(inr, usd, eur):
    return inr + usd*85 + eur*120

print(total(100, 1, 1)) # 305

curr = [100,1,1]
print(total(*curr))

curr = {"inr": 100, "usd": 1, "eur": 1}
print(total(**curr)) # 305

curr = {"inr": 100, "usd": 1, "eur": 1, "PNL": 100}
try:
    print(total(**curr)) # 305
except TypeError as e:
    print(e.args)
    print(e)

