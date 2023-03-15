import os
import time


def find_max_len(dish):
    size = 0
    for i in dish:
        if size < len(i):
            size = len(i)
    return size
def rating_desgin(stars):
    for i in range(stars):
        print("*" , end =" ")
def taking_user_data_for_Delivery():


    list =[]
    list.append(input("Name : "))
    list.append(input("Phone Number : "))
    list.append(input("Address : "))
    print("\t"*10 , end = "")
    size = find_max_len(list)
    print("-"*(size+40))
    type = ["Name", "Phone Number" , "Address"]
    for i in range(len(list)):
        print("{0}{2} : {1}".format("\t"*12  ,list[i],type[i] ))
    print("{0}Delivery Time : 30 min".format("\t"*12))
    print("\t"*10 , end = "")
    print("-"*(size+40))

def cancel_or_not():
    print("For Canceling order enter 0\nFor conforming order enter 1")
    command = int(input())
    if(command == 0):
        Service()
    else:
        taking_user_data_for_Delivery()

def takingOrder(menu_list  , price):
    print("Please Enter Count of food you want to order")
    count = int(input())
    order = []
    done = 1
    for i in range(count):
        position =input("Enter food number {0}: ".format(done))
        order.append(menu_list[int(position)-1])
        done+=1



    making_bill(order , price)
    cancel_or_not()
def making_bill(order_list , price):
    print("\t"*10 , end = "")
    size = find_max_len(order_list)
    print("-"*(size+40))
    count = 1
    total_amount = 0
    for i in range(len(order_list)):
       
        print("{1}{2}. {0}: Rs.{3}".format(order_list[i] , "\t"*12, count ,price[i]))
        count+= 1
        total_amount = total_amount+price[i]

    print("{1}Total Bill : Rs.{0}".format(total_amount , "\t"*12)  )
    print("\t"*10 , end = "")   
    print("-"*(size+40))

def Service():
    print("--------Welcome To Food Service  ---------")
    food_list = ["curry , rice", "Rajma Chawal", "Dal makhni with Roti", "Chaola Bhatura", "Masala Dosa"]
    max_len = -1
    food_list_2 = ["Non Veg Biryani", "Tandoori Chicken", "Seak Kabbab"]
    price1 = [123, 143, 150, 80, 90]
    price2 = [100, 200, 300]
    rating1 = [3,4,5,1,3]
    rating2 = [1,2,4]
    resturant_name = ["Punjabi Daba " ,"Sathi Daba","Punjabi Daba ","Punjabi Daba ","Punjabi Daba "]
    type = input("\nFor (veg only) type --> 0"
                 " \nFor (non veg) only type --> 1 "
                 "\nFor both type --> 2\n")
    print("Food Menu ->\n")
    print(" -"*20)
    if type == "0":
        count = 1
        for i in range(len(food_list)):
            max_len = find_max_len(food_list)
            print("|")
            print("|{3}. {0}{2} = Rs.{1}".format(food_list[i], price1[i], " " * (max_len - len(food_list[i]) + 3),count))
            print("| Rating : ", end="")

            rating_desgin(rating1[i])
            print()
            print("| Place : {0}".format(resturant_name[i]))
            print("| " , end = "")
            print("-"*10,end="\n")
            count+=1
        takingOrder(food_list ,price1)

    elif type == "1":
        for i in range(len(food_list_2)):
            max_len = find_max_len(food_list_2)
            print("{0}{2} = Rs.{1}".format(food_list_2[i], price2[i], " " * (max_len - len(food_list_2[i]) + 3)))
    elif type == "2":
        t1 = find_max_len(food_list)
        t2 = find_max_len(food_list_2)
        max_len = max(t1, t2)
        for i in range(len(food_list)):
            print("{0}{2} = Rs.{1}".format(food_list[i], price1[i], " " * (max_len - len(food_list[i]) + 3)))
        for i in range(len(food_list_2)):
            print("{0}{2} = Rs.{1}".format(food_list_2[i], price2[i], " " * (max_len - len(food_list_2[i]) + 3)))
    else:
        print("Give correct input")
    print(" -" * 20)
Service()
