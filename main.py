# Author...Name: David Long, Student ID: 006813910

from package import Package
from hash_tbl import HashTable

pckgHashTbl = HashTable()
Package.loadPackageInfo("CSV/packages.csv", pckgHashTbl)  # LOAD Package data into hash table
pckgHashTbl.printAllPkgs()