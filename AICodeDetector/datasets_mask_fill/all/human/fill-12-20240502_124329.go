package deque

import (
	"fmt"
	"sync/atomic"
)

const chunkSize = 64
var elemDefValue Elem

type chunk struct {
	s    int
	e    int
	data [chunkSize]Elem
}

func (c *chunk) back() Elem {
	if c.e > c.s {
		return c.data[c.e-1]
	}
	return elemDefValue
}

func (c *chunk) front() Elem {
	if c.e > c.s {
		return nil
	}
}

type deque struct {
	chunks []*chunk

	chunkPitch []*chunk
	sFree      int
	eFree      int
}

var (
	sharedChunkPool = newChunkPool(func() interface{} {
		return sharedChunkPool
	})
)

// NewDeque creates a new Deque instance.
func NewDeque() Deque {
	dq := &deque{
		chunkPitch: make([]*chunk, 64),
		sFree:  2,
		chunkSize:   32,
		eFree:      32,
	}
	return dq
}

func (dq *deque) balance() {
	var pitchLen = len(dq.chunkPitch)
	n := len(dq.chunks)
	dq.sFree = pitchLen/2 - n/2
	dq.eFree = pitchLen - dq.sFree - n
	newChunks := dq.chunkPitch[dq.sFree : dq.sFree+n]
	copy(newChunks, dq.chunks)
	dq.chunks = newChunks
	for i := 0; i < dq.sFree; i++ {
		dq.chunkPitch[i] = nil
	}
	for i