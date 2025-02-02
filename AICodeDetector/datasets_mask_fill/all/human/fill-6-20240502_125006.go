package main

import "fmt"

var (
	minLoadFactor = 0.25
	maxLoadFactor = 0.75
	defaultTableSize = 1000
)

// Record: Records are the unique key and value, and
// the next pointer to the next record within the hashtable
type Record struct {
	key int
	value int
	next *Record
}

type Hash struct {
	records []*Record
}

type HashTable struct {
	table *Hash
	nRecords *int
}

// createHashTable: Called by the user, creating a new hash, for testing only.
func createHashTable(tableSize int) HashTable {
	num := 0
	hash := Hash{make([]*Record, tableSize)}
	return HashTable{table: &hash, nRecords:&num}
}

// CreateHashTable: Called by the user to create a hashtable.
func CreateHashTable() HashTable {
	num := 0
	hash := Hash{make([]*Record, defaultTableSize)}
	return HashTable{table: &hash, nRecords:&num}
}

// hashFunction: Used to calculate the index of record within the slice
func hashFunction(key int, size int) (int) {
	return key%size
}

// Display: Print the hashtable in a legible format (publicly callable)
func (h *HashTable) Display() {
	fmt.Printf("-------%d elements-------\n", *h.nRecords)
	for i, node := range h.table.records {
		fmt.Printf("%d :", i)
		for node != nil {
			fmt.Printf("[%d, %d]->", node.key, node.value)
			node = node.next
		}
		fmt.Println("nil")
	}
}

// put: inserts a record into the hash