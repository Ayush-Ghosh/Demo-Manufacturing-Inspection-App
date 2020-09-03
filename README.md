# Demo-Manufacturing-Log-App

1. Git clone the repository.
2. PIP install the requirement.txt
3. First run db.py file. This script will push the data to mongodb and it will run for 30 mins.
4. Now open the db.py file and change sku="S1" to sku="S2" and run the code again. 
5. Repeat the above step for sku="S3", sku="S4", sku="S5", sku="S6", sku="S7" and sku="S8" in order to store 4 hours of data for every 30 mins interval.
6. Make sure that you've run the db.py script 8 times by changing the sku="S1", sku="S2" and so on till sku="S8", so that you've atleast 4 hours of data. You can run the same script 8 times at once also by changing the "sku" value, but it'll be computationally expensive and will consume high resources. 
7. In order to create multiple SKUs in Mongodb database, open db.py and change colname="SKU1" to colname="SKU2" or to anything as you like. Here, each collection is represented as one SKU. So change the collection name and run it similarly for 8 times by changing the "sku" value in a similar way as you've done it in above steps. Do it multiple times for different SKUs. 

8. Now run the main_ui.py file to open up the GUI.

# NOTE #
Make sure you've followed the steps mentioned and have atleast 4 hours of data for every 30 mins interval before you run main_ui.py file or else the barchart will have null plottings and might crash the application in any exceptional case.

# SCREENSHOTS #
