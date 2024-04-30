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
func (s *Set) Add(val <extra_id_0> s.myset[val] <extra_id_1> (s *Set) Has(val <extra_id_2> {
 if _, ok := s.myset[val]; ok {
  return true
 <extra_id_3> {
  return false
 }
}
func (s *Set) SetToSlice() []int <extra_id_4> maps.Keys(s.myset)
}

func FindIntersectingElements(arr1, arr2 []int) []int {
	set1 := CreateSet()
	for _, <extra_id_5> range arr1 {
	 if !set1.Has(val) {
	  set1.Add(val)
	 }
	}
	intersectionSet := CreateSet()
	for _, val := range arr2 {
	 if set1.Has(val) <extra_id_6> intersectionSet.Add(val)
	 }
	}
	return intersectionSet.SetToSlice()
   }
   

func main() {
	res := FindIntersectingElements([]int{4, 1, 4, 7, 4}, []int{7, <extra_id_7> 6, 4, 7, 4})
	fmt.Println(res)
}
