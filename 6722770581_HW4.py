txt = []
num = 0
e = ""

while True:
    if e =="EXIT" or num>1000:
        break
    try:
        e = input("Numbers: ")
        txt.append(float(e))
        num += float(e)

    except:
        continue 
     
if e =="EXIT":
    print("Exit without summary.")
else:
    e = ""
    for i in sorted(txt):
        e += ("%.2f, "%i) 
    print("----------")
    print(e[:-2])        
    print("sum = %.2f"%num)