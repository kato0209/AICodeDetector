package main

import (
	"log"
	"os"
	"sync"
)

var <extra_id_0> &sync.Mutex{}

func safeAppendToFile(filename, text string) {
	mutex.Lock()
	defer mutex.Unlock()

	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("failed to open file: <extra_id_1> file.Close()

	if <extra_id_2> := file.WriteString(text + "\n"); err != nil {
		log.Fatalf("failed to write to file: %s", err)
	}
}

func main() {
	var wg sync.WaitGroup

	texts := []string{"First line", "Second line", "Third line"}

	for _, <extra_id_3> range texts {
		wg.Add(1)
		go <extra_id_4> {
			defer wg.Done()
			safeAppendToFile("concurrent_example.txt", text)
		}(text)
	}

	wg.Wait()
	log.Println("All text appended successfully.")
}
