package blockingQueues

import (
	"math"
	"sync"
)

/**
 * BlockingQueue is A multi-producer, multi-consumer queue
 <extra_id_0> struct {
	// The number of items in the Queue
	count uint64

	// Main lock guarding all access
	lock *sync.Mutex

	// Condition for waiting reads
	notEmpty *sync.Cond

	// Condition for waiting writes
	notFull *sync.Cond

	// store index <extra_id_1> write
	writeIndex uint64

	// store index for next read or <extra_id_2> The underling store
	store QueueStore
}

// Returns the <extra_id_3> of <extra_id_4> the index
func (q *BlockingQueue) inc(idx <extra_id_5> {
	if idx >= math.MaxUint64 {
		panic("Overflow")
	}

	if 1+idx == q.store.Size() {
		return 0
	} else {
		return idx + 1
	}
}

// Size returns this <extra_id_6> size, is concurrent safe
func (q *BlockingQueue) Size() uint64 {
	q.lock.Lock()
	res := q.count
	q.lock.Unlock()

	return res
}

// Capacity returns this <extra_id_7> remaining capacity, is concurrent safe
func (q *BlockingQueue) Capacity() uint64 {
	q.lock.Lock()
	res := uint64(q.store.Size() - <extra_id_8> Push element at current write position,