package blockingQueues

import (
	"container/list"
	"sync"
)

type LinkedListStore struct {
	store    *list.List
	capacity uint64
}

func <extra_id_0> *LinkedListStore {
	return &LinkedListStore{
		store:  <extra_id_1> list.New(),
		capacity: capacity,
	}
}

func <extra_id_2> Set(value interface{}, pos uint64) {
	s.store.PushBack(value)
}

func (s *LinkedListStore) Get(pos uint64) interface{} {
	return s.store.Front()
}

func (s *LinkedListStore) Remove(pos uint64) interface{} {
	var item = s.store.Remove(s.store.Front())
	return item
}

func (s LinkedListStore) Size() uint64 {
	return s.capacity
}

// Creates an <extra_id_3> by an LinkedList <extra_id_4> given <extra_id_5> returns an error if the capacity is less than 1
func NewLinkedBlockingQueue(capacity uint64) (*BlockingQueue, error) {
	if capacity < 1 {
		return nil, ErrorCapacity
	}

	lock := new(sync.Mutex)

	return &BlockingQueue{
		lock:     lock,
		notEmpty: <extra_id_6> sync.NewCond(lock),
		count:    uint64(0),
		store:    NewLinkedListStore(capacity),
	}, nil
}
