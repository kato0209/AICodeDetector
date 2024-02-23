package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	tasks := []string{
		"Feed-forward neural networks",
		"convolutional neural networks",
		"graph neural networks",
		"Boyer Moore algorithm",
		"Dijkstra algorithm",
		"greatest common division",
		"Levenshtein",
		"logistic regression",
		"matrix multiplication",
		"Rocchio algorithm",
		"SVM",
		"Append text",
		"concatenate file",
		"Excel file",
		"read file",
		"read file list",
		"write file",
		"copy file",
		"get modified time",
		"MP3 file",
		"Email",
		"HTTP client/server",
		"FTP client/server",
		"chat client/server",
		"Binary search",
		"exponential search",
		"sequential search",
		"breadth-first search",
		"depth-first search",
		"linear search",
		"bubble sort",
		"merge sort",
		"Array blocking issue",
		"compare two strings",
		"delete word",
		"dequeue",
		"common elements",
		"minimum element",
	}

	randIndex := rand.Intn(len(tasks))
	chosenTask := tasks[randIndex]

	fmt.Printf("Chosen task: %s\n", chosenTask)
}