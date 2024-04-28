package main

import (
	"log"
	"os"
	"sync"
)

var mutex = &sync.Mutex{}

func safeAppendToFile(filename, text string) {
	mutex.Lock()
	defer mutex.Unlock()

	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	if _, err := file.WriteString(text + "\n"); err != nil {
		log.Fatalf("failed to write to file: %s", err)
	}
}

func main() {
	var wg sync.WaitGroup

	texts := []string{"First line", "Second line", "Third line"}

	for _, text := range texts {
		wg.Add(1)
		go func(text string) {
			defer wg.Done()
			safeAppendToFile("concurrent_example.txt", text)
		}(text)
	}

	wg.Wait()
	log.Println("All text appended successfully.")
}
