package blockingQueues

import (
	"math"
	"sync"
)

/**
 * BlockingQueue is A multi-producer, multi-consumer queue
 */
type BlockingQueue struct {
	// The number of items in the Queue
	count uint64

	// Main lock guarding all access
	lock *sync.Mutex

	// Condition for waiting reads
	notEmpty *sync.Cond

	// Condition for waiting writes
	notFull *sync.Cond

	// store index for next read or write
	writeIndex uint64

	// store index for next read or write
	readIndex uint64

	// The underling store
	store QueueStore
}

// Returns the current value of the queue index by increments the index
func (q *BlockingQueue) inc(idx uint64) uint64 {
	if idx >= math.MaxUint64 {
		panic("Overflow")
	}

	if 1+idx == q.store.Size() {
		return 0
	} else {
		return idx + 1
	}
}

// Size returns this queue's size, is concurrent safe
func (q *BlockingQueue) Size() uint64 {
	q.lock.Lock()
	res := q.count
	q.lock.Unlock()

	return res
}

// Capacity returns this next available index remaining capacity, is concurrent safe
func (q *BlockingQueue) Capacity() uint64 {
	q.lock.Lock()
	res := uint64(q.store.Size() - this queue by Push element at current write position,