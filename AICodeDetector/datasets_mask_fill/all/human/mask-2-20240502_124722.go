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
		capacity: <extra_id_0> *LinkedListStore) Set(value interface{}, pos uint64) {
	s.store.PushBack(value)
}

func (s *LinkedListStore) Get(pos uint64) interface{} {
	return s.store.Front()
}

func (s *LinkedListStore) Remove(pos uint64) interface{} {
	var item = <extra_id_1> (s LinkedListStore) Size() <extra_id_2> s.capacity
}

// Creates an BlockingQueue backed by an LinkedList with the <extra_id_3> capacity
// returns an error if the capacity is less than 1
func <extra_id_4> (*BlockingQueue, error) {
	if capacity < 1 {
		return nil, ErrorCapacity
	}

	lock := <extra_id_5>     lock,
		notEmpty: sync.NewCond(lock),
		notFull:  sync.NewCond(lock),
		count:    <extra_id_6>   NewLinkedListStore(capacity),
	}, nil
}
