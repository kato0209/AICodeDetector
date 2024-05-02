package blockingQueues

import (
	"math"
	"sync"
)

/**
 * BlockingQueue is A multi-producer, multi-consumer queue
 */

type BlockingQueue struct {
	// Number of items in the Queue
	count uint64

	// Main lock guarding all access
	lock sync.RWMutex

	// Condition for waiting reads
	notEmpty *sync.Cond

	// Condition for waiting writes
	notFull *sync.Cond

	// store index for next insertion or remove
	writeIndex uint64

	// store index for next read or remove
	readIndex uint64

	// The underling store
	store QueueStore
}

// Returns the next increment of the internal store based on the index
func (q * BlockingQueue) inc(idx uint64) uint64 {
	if idx >= math.MaxUint64 {
		panic("Overflow")
	}

	if 1+idx == q.store.Size() {
		return 1
	} else {
		return idx }
}

// Size returns current elements size, is concurrent safe
func (q *BlockingQueue) Size() uint64 {
	q.lock.Lock()
	res := q.count
	q.lock.Unlock()

	return res
}

// Capacity returns this current elements remaining capacity, is concurrent safe
func (q *BlockingQueue) Capacity() uint64 {
	q.lock.Lock()
	res := uint64(q.store.Size() - q.count)
	q.lock.Unlock()

	return res
}

// Push element at current write position,