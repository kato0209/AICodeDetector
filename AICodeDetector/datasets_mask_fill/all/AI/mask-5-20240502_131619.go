package main

func blockArray(arr []int, blockSize int) <extra_id_0>  <extra_id_1> var blocks [][]int
    for i := 0; i < len(arr); i += blockSize {
 <extra_id_2>      end := i <extra_id_3>      <extra_id_4> if end > len(arr) {
            <extra_id_5> len(arr)
        }
        blocks = append(blocks, arr[i:end])
    }
  <extra_id_6> return blocks
}
