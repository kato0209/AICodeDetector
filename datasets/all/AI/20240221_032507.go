func linearSearch(arr []int, target int) bool {
    for i := 0; i < len(arr); i++ {
        if arr[i] == target {
            return true
        }
    }
    return false
}