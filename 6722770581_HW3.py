coffeeDB = [['C','Signature Chocolate',130],
            ['M','Matcha Latte',125],
            ['A','Americano',120],
            ['R','Iced Raspberry Juice Tea',115],
            ['O','Sai Nam Pueng Orange Juice',95],
            ['E','Espresso',50]]
txt = []
summ_item = {}
print("Beverage Menu")
print("-"*56)
print("| %-3s | %-4s | %-30s | %-6s |" % ("No.","Code","Item Name","Price"))
print("-"*56)
for i, val in enumerate(coffeeDB):
    print("| %2d. | %-4s | %-30s | %6.2f |" % (int(i+1),val[0],val[1],val[2]))
print("-"*56)

order = input("User's orders: ").upper()
for i in order:
    if i in "CMAROE":
        txt.append(i)
            
        if i in summ_item:
            summ_item[i] += 1  
        else:
            summ_item[i] = 1   
    else:
        print("skipping NOCODE (%s)" % i)
if txt == []:
    print("NO ORDER!!!")
else:
    sub =0
    print("Bill summary")
    print("-" * 56)
    print("| %-3s | %-30s | %-4s | %-6s |" % ("NO.", "ITEM NAME", "QTY", "AMOUNT"))
    print("-" * 56)
    for i, (code, qty) in enumerate(sorted(summ_item.items())):
        item = next((x for x in coffeeDB if x[0] == code), None)
        if item:
            item_name = item[1]
            price = item[2]
            amount = price * qty
            sub += amount
            print("| %2d. | %-30s | %-4d | %6.2f |" % (i+1, item_name, qty, amount))
    vat = sub * 0.07
    tot = sub + vat
    print("-" * 56)
    print("| %-44s| %6.2f |"%(("Subtotal"),sub))
    print("| %-44s| %6.2f |"%(("Total tax"),vat))
    print("| %-44s| %6.2f |"%(("Total"),tot))
    print("-" * 56)
