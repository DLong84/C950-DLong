# Author...Name: David Long, Student ID: 006813910
import datetime

from package import Package
from hash_tbl import HashTable
from truck import Truck

pckgHashTbl = HashTable()
Package.loadPackageInfo("CSV/packages.csv", pckgHashTbl)  # LOAD Package data into hash table
pckgHashTbl.printAllPkgs()

