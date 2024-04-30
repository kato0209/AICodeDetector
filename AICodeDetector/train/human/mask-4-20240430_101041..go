package <extra_id_0> (
	minLoadFactor = 0.25
	maxLoadFactor <extra_id_1> = 3
)

type Record struct <extra_id_2> int
	next *Record
}

type Hash struct {
	records []*Record
}

type HashTable struct <extra_id_3> *int
}

// createHashTable: Called by checkLoadFactorAndUpdate when creating a new hash, <extra_id_4> use only.
func createHashTable(tableSize int) HashTable {
	num := 0
	hash := Hash{make([]*Record, <extra_id_5> &hash, nRecords:&num}
}

// CreateHashTable: Called by the user to create a hashtable.
func CreateHashTable() HashTable {
	num := 0
	hash := Hash{make([]*Record, defaultTableSize)}
	return HashTable{table: &hash, nRecords:&num}
}

// hashFunction: Used to calculate the <extra_id_6> record within the slice
func <extra_id_7> size int) (int) {
	return key%size
}

// Display: Print the hashtable in a legible format (publicly callable)
func (h *HashTable) Display() {
	fmt.Printf("----------%d elements-------\n", *h.nRecords)
	for i, node <extra_id_8> h.table.records {
		fmt.Printf("%d :", i)
		for node != nil {
			fmt.Printf("[%d, %d]->", node.key, node.value)
			node = node.next
		}
		fmt.Println("nil")
	}
}

// put: inserts a key into the hash