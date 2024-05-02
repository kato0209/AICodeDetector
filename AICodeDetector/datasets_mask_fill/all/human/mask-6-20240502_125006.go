package main

import "fmt"

var (
	minLoadFactor = 0.25
	maxLoadFactor = 0.75
	defaultTableSize = <extra_id_0> struct {
	key int
	value int
	next *Record
}

type Hash struct {
	records []*Record
}

type HashTable <extra_id_1> *Hash
	nRecords *int
}

// createHashTable: Called by <extra_id_2> creating a new hash, for <extra_id_3> only.
func createHashTable(tableSize int) <extra_id_4> := <extra_id_5> Hash{make([]*Record, tableSize)}
	return HashTable{table: &hash, nRecords:&num}
}

// CreateHashTable: Called by the user to create a hashtable.
func CreateHashTable() HashTable {
	num := <extra_id_6> Hash{make([]*Record, defaultTableSize)}
	return HashTable{table: &hash, nRecords:&num}
}

// hashFunction: Used to calculate the index of record within the slice
func hashFunction(key int, size int) (int) {
	return key%size
}

// Display: Print the hashtable in a legible format (publicly callable)
func (h *HashTable) <extra_id_7> elements-------\n", *h.nRecords)
	for i, node := range h.table.records {
		fmt.Printf("%d :", i)
		for node != nil {
			fmt.Printf("[%d, %d]->", node.key, node.value)
			node = node.next
		}
		fmt.Println("nil")
	}
}

// put: inserts <extra_id_8> into the hash