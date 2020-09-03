import pymongo
import time

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["BottlePlant"]

colname = "SKU1"                     #change the collection name to change the SKU. SKUs are maintained as different collections and each
                                     #collection represents one SKU
col = db[colname] 

sku = "S1"                          # Keep Changing sku. Eg. sku = "S2" after every 30 mins.
                                    #Start from "S1" and change this to "S2" then "S3" then "S4", "S5", "S6", "S7" and so on till "S8" after every 30 mins and run this code again
                                    #to keep pushing the data for 4 hrs in every 30 mins of interval
                                
uid = 0

status = "Good"
t_end = time.time() + 60 * 30   # this loop will run for 30 minutes i.e 1800 seconds

while time.time() < t_end:
    uid = uid+1                  #incrementing the unit id everytime
    if uid<=5400:                 #assigning 90% value good and rest as bad(keep modifying the uid value to 80% to see a noticable change in thr graph)
        status = "Good"
    else:
        status = "Bad"
 
    data = {"SKU id":sku, "Unit id":uid, "Timestamp":time.ctime(), "Status":status}
    x = col.insert_one(data)
    time.sleep(300/1000)        #pushing data to db every 300ms
    print("data recorded")

print("done")