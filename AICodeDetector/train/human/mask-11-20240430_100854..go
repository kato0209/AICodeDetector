<extra_id_0> (
	"fmt"
	"sync/atomic"
)

const chunkSize = 254

var elemDefValue Elem

type chunk struct {
	s    int
	e <extra_id_1>  <extra_id_2> (c *chunk) back() Elem {
	if c.e <extra_id_3> {
		return c.data[c.e-1]
	}
	return elemDefValue
}

func (c *chunk) front() Elem {
	if c.e <extra_id_4> {
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
	dq <extra_id_5> make([]*chunk, 64),
		sFree:      32,
		eFree:      32,
	}
	return dq
}

func (dq *deque) balance() {
	var pitchLen = len(dq.chunkPitch)
	n <extra_id_6> = pitchLen/2 - n/2
	dq.eFree = pitchLen - dq.sFree - n
	newChunks := dq.chunkPitch[dq.sFree : <extra_id_7> = newChunks
	for i := 0; i < dq.sFree; i++ <extra_id_8> nil
	}
	for i