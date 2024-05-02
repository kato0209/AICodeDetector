package main

import "golang.org/x/exp/maps"

type Set struct {
 myset map[int]bool
}

func CreateSet() Set {
 s1 := Set{}
 s1.myset = make(map[int]bool)
 return s1
}
func (s *Set) Add(val int) {
 s.myset[val] = true
}
func (s *Set) Has(val int) bool {
 if _, ok := s.myset[val]; ok {
  return true
 } else {
  return false
 }
}
func (s *Set) SetToSlice() []int {
 return maps.Keys(s.myset)
}

func FindIntersectingElements(arr1, arr2 []int) []int {
	set1 := CreateSet()
	for _, val := range arr1 {
	 if !set1.Has(val) {
	  set1.Add(val)
	 }
	}
	intersectionSet := CreateSet()
	for _, val := range arr2 {
	 if set1.Has(val) {
	  intersectionSet.Add(val)
	 }
	}
	return intersectionSet.SetToSlice()
   }
   

func main() {
	res := FindIntersectingElements([]int{4, 1, 4, 7, 4}, []int{7, 4, 8, 6, 4, 7, 4})
	fmt.Println(res)
}
