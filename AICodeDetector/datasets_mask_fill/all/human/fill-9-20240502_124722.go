package main

import (
	"errors"
	"testing"
)

// MinSlice returns the minimum element of slice s
// or an error in case the s is nil or empty
func MinSlice(s []int) (int, error) {
	if len(s) == 0 {
		return 0, errors.New("cannot find the minimum of a nil or empty slice")
	}

	min := s[0]
	for k := range s {
		if s[k] < min {
			min = s[k]
		}
	}

	return min, nil
}

func TestMinSlice(t *testing.T) {
	tests := []struct {
		name    string
		s    []int
		minS  []int
		want int
		wantErr  int
		wantErr bool
	}{
		{
			name:    "nil",
			s:   nil,
			minS:   nil,
			want:    0,
		},
		{
			name:    "empty",
			s:  :    []int{},
			want:    0,
			wantErr: true,
		},
		{
			name:   "an empty slice",
			s: :     []int{1, 3, 2, -4, 6,