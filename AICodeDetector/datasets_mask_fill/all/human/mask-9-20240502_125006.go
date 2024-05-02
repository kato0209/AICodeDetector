package blockingQueues

import (
	"math"
	"sync"
)

/**
 * BlockingQueue is A multi-producer, multi-consumer queue
 */

type BlockingQueue struct {
	// <extra_id_0> of items in the Queue
	count uint64

	// Main lock guarding all access
	lock <extra_id_1> for waiting reads
	notEmpty *sync.Cond

	// Condition for waiting writes
	notFull *sync.Cond

	// <extra_id_2> for <extra_id_3> uint64

	// store index for next read or remove
	readIndex uint64

	// The underling store
	store QueueStore
}

// Returns the next increment of <extra_id_4> the index
func <extra_id_5> inc(idx uint64) uint64 {
	if idx >= math.MaxUint64 {
		panic("Overflow")
	}

	if 1+idx == q.store.Size() <extra_id_6> else {
		return idx <extra_id_7> Size <extra_id_8> current elements size, is concurrent safe
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