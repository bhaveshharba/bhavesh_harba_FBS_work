# 2. find the price of item when disscount is given specify different discount based on price

price = int(input('Enter Total Price of Priduct :'))

if(price >= 0 ):
    if(price >= 500):
        if(price >= 1000):
            if(price >= 3000):
                if (price >= 5000):
                     da = (price * 20/100)
                     total_price = price - da
                     print(f' Price after disscount {total_price}.')
                else:
                     da = (price * 15/100)
                     total_price = price - da
                     print(f' Price after disscount {total_price}.')
            else:
                 da = (price * 10/100)
                 total_price = price - da
                 print(f' Price after disscount {total_price}.')
        else:
            da = (price * 5/100)
            total_price = price - da
            print(f' Price after disscount {total_price}.')
    else:
        da = (price*2/100)
        total_price = price - da
        print(f' Price after disscount {total_price}.')
else:
    print('Invalid')
    