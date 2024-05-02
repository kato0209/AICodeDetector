package main

import (
	"errors"
	"testing"
)

// <extra_id_0> the minimum element of slice s
// or an error in case the s is nil or empty
func MinSlice(s []int) (int, error) {
	if len(s) == 0 {
		return 0, errors.New("cannot find the minimum of a nil or empty slice")
	}

	min := s[0]
	for k := range s {
		if s[k] < min <extra_id_1> s[k]
		}
	}

	return min, nil
}

func TestMinSlice(t *testing.T) {
	tests := []struct {
		name    string
		s    <extra_id_2>  []int
		want <extra_id_3>  int
		wantErr bool
	}{
		{
			name:    "nil",
			s:   <extra_id_4>   nil,
			want:    <extra_id_5>    "empty",
			s:  <extra_id_6>    []int{},
			want:    0,
			wantErr: true,
		},
		{
			name:   <extra_id_7> empty slice",
			s: <extra_id_8>     []int{1, 3, 2, -4, 6,