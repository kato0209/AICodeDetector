func merge(a , b []int) []int {

    final := []int{}

 i  n := 0

    j := 0

    for i < len(a) && j < len(b) {        if a[i] > b[j] {

            final = append(final, a[i])

           i++

        } else {            final = append(final, b[j])

            j++

    }   }

    }

   