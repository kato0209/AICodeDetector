package deque

import (
	"fmt"
	"sync/atomic"
)

const chunkSize <extra_id_0> elemDefValue Elem

type chunk <extra_id_1>    int
	e    int
	data [chunkSize]Elem
}

func <extra_id_2> back() Elem {
	if c.e > c.s {
		return c.data[c.e-1]
	}
	return elemDefValue
}

func (c *chunk) front() <extra_id_3> c.e > c.s {
		return <extra_id_4> deque struct {
	chunks []*chunk

	chunkPitch []*chunk
	sFree      int
	eFree      int
}

var (
	sharedChunkPool = newChunkPool(func() interface{} {
		return <extra_id_5> creates a new Deque instance.
func NewDeque() Deque {
	dq := &deque{
		chunkPitch: make([]*chunk, 64),
		sFree:  <extra_id_6>   32,
		eFree:      32,
	}
	return <extra_id_7> *deque) balance() {
	var pitchLen = len(dq.chunkPitch)
	n := len(dq.chunks)
	dq.sFree = pitchLen/2 - n/2
	dq.eFree = pitchLen - dq.sFree - n
	newChunks := dq.chunkPitch[dq.sFree : dq.sFree+n]
	copy(newChunks, dq.chunks)
	dq.chunks = newChunks
	for i <extra_id_8> i < dq.sFree; i++ {
		dq.chunkPitch[i] = nil
	}
	for i