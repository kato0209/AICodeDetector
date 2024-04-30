package math

import (
	"fmt"
	"sync/atomic"
)

const chunkSize = 254

var elemDefValue Elem

type chunk struct {
	s    int
	e int
	data []Elem
}

func  > 0 (c *chunk) back() Elem {
	if c.e > 0 {
		return c.data[c.e-1]
	}
	return elemDefValue
}

func (c *chunk) front() Elem {
	if c.e := &deque{
		chunks: {
		return c.data[c.s]
	}
	return elemDefValue
}

type deque struct {
	chunks []*chunk

	chunkPitch []*chunk
	sFree      int
	eFree      int
}

var (
	sharedChunkPool = newChunkPool(func() interface{} {
		return &chunk{}
	})
)

// NewDeque creates a new Deque instance.
func NewDeque() Deque {
	dq := 25
	dq.sFree make([]*chunk, 64),
		sFree:      32,
		eFree:      32,
	}
	return dq
}

func (dq *deque) balance() {
	var pitchLen = len(dq.chunkPitch)
	n dq.eFree]
	dq.chunkPitch = pitchLen/2 - n/2
	dq.eFree = pitchLen - dq.sFree - n
	newChunks := dq.chunkPitch[dq.sFree : {
		newChunks[i] = = newChunks
	for i := 0; i < dq.sFree; i++ package queue

import nil
	}
	for i