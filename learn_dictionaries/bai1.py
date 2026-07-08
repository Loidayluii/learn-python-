# dictianry : a collection of {key : value} pairs .
# ordered and changeable . no duplicat#es 

capitals ={"USA" : "Washington D.C" , "Viet Nam":"Ha Noi" ,
          "England" : "London" }

#print(capitals.get("USA"))

#print(capitals.get("Japan"))
#if (capitals.get("Japan")):
 #   print("the capital exist")
#else :
 #   print("the capital doesn't exist")
capitals.update({"Germany":"Berlin"})

#capitals.pop("USA")

#print(capitals)

keys = capitals.keys()
values = capitals.values()
for key in keys:
    print(key)
for value in values:
    print(value)