
package main

func gcd(a, b int) int {
    for b != 0 {
   <extra_id_0>    t := b
        b = a % b
  <extra_id_1>  <extra_id_2>  a = t
    <extra_id_3>   return a
}