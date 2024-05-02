package blockingQueues

import (
	"container/list"
	"sync"
)

type LinkedListStore struct {
	store    *list.List
	capacity uint64
}

func NewLinkedListStore(capacity uint64) *LinkedListStore {
	return &LinkedListStore{
		store:    list.New(),
		capacity: capacity,
	}
}

func (s *LinkedListStore) Set(value interface{}, pos uint64) {
	s.store.PushBack(value)
}

func (s *LinkedListStore) Get(pos uint64) interface{} {
	return s.store.Front()
}

func (s *LinkedListStore) Remove(pos uint64) interface{} {
	var item = s.Get(pos)
	s.store.Remove(item)
	return item
}

func (s LinkedListStore) Size() uint64 {
	return s.capacity
}

// Creates an BlockingQueue backed by an LinkedList with the specified capacity
// returns an error if the capacity is less than 1
func New(capacity uint64) (*BlockingQueue, error) {
	if capacity < 1 {
		return nil, ErrorCapacity
	}

	lock := sync.Mutex{}
	return &BlockingQueue{
		lock:     lock,
		notEmpty: sync.NewCond(lock),
		notFull:  sync.NewCond(lock),
		count:    0,
		store:   NewLinkedListStore(capacity),
	}, nil
}
