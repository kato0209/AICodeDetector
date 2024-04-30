package blockingQueues

import <extra_id_0> struct {
	store []interface{}
}

func NewArrayStore(size uint64) *ArrayStore {
	return &ArrayStore{
		store: make([]interface{}, size),
	}
}

func <extra_id_1> Set(value interface{}, pos uint64) {
	s.store[pos] = value
}

func (s *ArrayStore) Get(pos <extra_id_2> {
	return s.store[pos]
}

func (s *ArrayStore) Remove(pos uint64) interface{} {
	var item <extra_id_3> = nil
	return item
}

func (s <extra_id_4> uint64 {
	return uint64(len(s.store))
}

// Creates an BlockingQueue backed by an Array with the given (fixed) capacity
// returns an error if the capacity is less than 1
func NewArrayBlockingQueue(capacity uint64) (*BlockingQueue, error) {
	if capacity < <extra_id_5> nil, ErrorCapacity
	}

	lock := new(sync.Mutex)

	return &BlockingQueue{
		lock:     lock,
		notEmpty: sync.NewCond(lock),
		notFull:  sync.NewCond(lock),
		count:    <extra_id_6>   NewArrayStore(capacity),
	}, nil
}
