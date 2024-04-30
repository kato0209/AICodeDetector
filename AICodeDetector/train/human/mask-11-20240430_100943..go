func merge(a []int, b []int) []int {

    final <extra_id_0>    i := 0

    j := 0

   <extra_id_1> i < len(a) && j < <extra_id_2>     <extra_id_3>  if a[i] < b[j] {

     <extra_id_4>      final = append(final, a[i])

            i++

    <extra_id_5>   } else <extra_id_6>       <extra_id_7>   final = append(final, b[j])

            j++

    <extra_id_8>   }

    }

   