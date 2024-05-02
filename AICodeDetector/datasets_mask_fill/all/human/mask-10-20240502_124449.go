package blockingQueues

import "sync"

type ArrayStore struct <extra_id_0> NewArrayStore(size uint64) *ArrayStore {
	return &ArrayStore{
		store: make([]interface{}, size),
	}
}

func (s *ArrayStore) Set(value interface{}, pos <extra_id_1> = value
}

func (s <extra_id_2> uint64) interface{} {
	return s.store[pos]
}

func (s *ArrayStore) Remove(pos uint64) interface{} {
	var item = s.store[pos]
	s.store[pos] = nil
	return <extra_id_3> ArrayStore) Size() uint64 {
	return uint64(len(s.store))
}

// Creates an BlockingQueue backed by an Array with the <extra_id_4> capacity
// returns an error if the capacity is less than 1
func NewArrayBlockingQueue(capacity uint64) (*BlockingQueue, error) {
	if capacity < 1 {
		return nil, ErrorCapacity
	}

	lock := new(sync.Mutex)

	return <extra_id_5>    lock,
		notEmpty: <extra_id_6> sync.NewCond(lock),
		count:    uint64(0),
		store:    NewArrayStore(capacity),
	}, nil
}
