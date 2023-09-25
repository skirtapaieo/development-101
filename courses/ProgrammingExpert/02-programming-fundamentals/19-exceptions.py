
""" try: 
    int("hej")
except: 
    print("haj")
 """

""" try: 
    2 / 0 
    int("hej") 
except ValueError as e: 
    print("Value exception", e)
except ZeroDivisionError as e: 
    print("Zero divison error!", e)
print("done")
 """

""" try: 
    2 / 0 
    int("hej") 
except Exception as e: 
    print("Exception", e)
finally: 
    print("done")
 """

#raise ValueError("This is a value error!"
                
raise Exception("This is an error!")
