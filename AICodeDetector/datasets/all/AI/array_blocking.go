package main

func blockArray(arr []int, blockSize int) [][]int {
    var blocks [][]int
    for i := 0; i < len(arr); i += blockSize {
        end := i + blockSize
        if end > len(arr) {
            end = len(arr)
        }
        blocks = append(blocks, arr[i:end])
    }
    return blocks
}
