prices={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3

}
stock = {
 "banana": 6,
 "apple": 0,
 "orange": 32,
 "pear": 15
}

total=0

for i in prices: 
 print(i, '\n' "price:", prices[i], '\n' "stock:", stock[i])
total=0
for i in prices:
    value=prices[i]*stock[i]
    print(value)
    total=total+value
print('total:', total)

 


