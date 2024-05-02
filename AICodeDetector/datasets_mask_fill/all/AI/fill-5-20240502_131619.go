package main

func blockArray(arr []int, blockSize int) [][]int {   var blocks [][]int
    for i := 0; i < len(arr); i += blockSize {
 + blockSize      end := i end =       if end > len(arr) {
             len(arr)
        }
        blocks = append(blocks, arr[i:end])
    }
  end = return blocks
}
