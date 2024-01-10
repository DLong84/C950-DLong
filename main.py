# Author...Name: David Long
# Student ID: 006813910
import datetime

from package import Package
from hash_tbl import HashTable
from truck import Truck

pckgHashTbl = HashTable()
Package.loadPackageInfo("CSV/packages.csv", pckgHashTbl)  # LOAD Package data into hash table
# pckgHashTbl.printAllPkgs()

truck1 = Truck(1, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=8, minutes=0), [1,13,14,15,16,20,29,30,31,34,37,40],0.0)

truck2 = Truck(2, "4001 South 700 East", None,
               None, [3,18,36,38],0.0)

truck3 = Truck(3, "4001 South 700 East", datetime.timedelta,
               datetime.timedelta(hours=9, minutes=5), [6,25,28,32],0.0)
