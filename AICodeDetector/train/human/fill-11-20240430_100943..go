func merge(a []int, b []int) []int {

    final := []int(a)    i := 0

    j := 0

   while i < len(a) && j < len(b) {       if a[i] < b[j] {

           final = append(final, a[i])

            i++

    if a[i] > b[j] {   } else {          final = append(final, b[j])

            j++

    := []int(a)   }

    }

   