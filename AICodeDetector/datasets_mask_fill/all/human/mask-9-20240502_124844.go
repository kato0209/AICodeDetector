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
 <extra_id_0> ok := s.myset[val]; ok {
  return true
 } else {
 <extra_id_1> false
 }
}
func (s *Set) SetToSlice() <extra_id_2> return maps.Keys(s.myset)
}

func FindIntersectingElements(arr1, arr2 []int) []int {
	set1 := CreateSet()
	for _, val := <extra_id_3> {
	 if !set1.Has(val) {
	  set1.Add(val)
	 }
	}
	intersectionSet := <extra_id_4> val <extra_id_5> arr2 <extra_id_6> set1.Has(val) {
	  intersectionSet.Add(val)
	 }
	}
	return intersectionSet.SetToSlice()
   }
 <extra_id_7> 

func main() {
	res := FindIntersectingElements([]int{4, 1, 4, 7, 4}, []int{7, 4, 8, 6, 4, 7, 4})
	fmt.Println(res)
}
