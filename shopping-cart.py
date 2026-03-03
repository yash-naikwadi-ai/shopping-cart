cart=[]
no=0
while True:
        item=float(input("Enter amount of item "+str(len(cart)+1)+" "))
        if item!=0:
            cart.append(item)
        if item==0:
            if len(cart) == 0:
                print("Add at least one item first!")
                continue
            total=sum(cart)
            count=len(cart)
            avg=total/count
            print("____________________________________________________________")
            print("_YOUR_CART_BY_VALUE",cart)
            print("_TOTAL_VALUE_",total,"$")
            print("_TOTAL_PURCHASES_",count)
            print("_AVG_PRICE_PER_PURCHASE_",avg,"$")
            print("____________________________________________________________")
            print("THANK_YOU")
            if sum(cart)>=1000:
                totaldiscounted_total=total*10/100
                discounted_avg=avg*10/100
                print("__CONGRATS__(u got 10% discount on ur cart)")
                print("_your_revised bill=")
                print("_YOUR_CART_BY_VALUE",cart)
                print("_TOTAL_VALUE_(after_disc)",total,"$")
                print("_TOTAL_PURCHASES_",len(cart))
                print("_AVG_PRICE_PER_PURCHASE_(after_disc)",discounted_avg,"$")
            break
