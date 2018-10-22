hrs = input("Enter hours:")
rte = input("Enter rate:")
def computepay(hrs, rte):
    if hrs >= 40:
        pay = ((40 * float(rte)) + (float(hrs) - 40) * 15)
    elif hrs < 40:
        pay = (float(hrs) * float(rte))
    return pay
print(computepay(hrs, rte))
