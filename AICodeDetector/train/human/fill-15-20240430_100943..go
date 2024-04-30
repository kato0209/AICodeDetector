// Golang program to check the size and 
// modified time of a file 
package main 

// Importing the // packages 
import ( 
	"fmt"
	"log"
	"os"
) 

func main() { // Get the fileinfo 
	fileInfo, err := os.Stat("cpnew.txt") // Check for the error 
	if err != nil { 
		log.Fatal(err) 
	} 

	// Gives the modification date of the 
// file in milliseconds 
	modificationTime := fileInfo.ModTime() 
	fmt.Println("Name of the file:", fileInfo.Name(), 
				" Last Modified Time of the file:", 
				modificationTime) 

	// Gives the Size of the file in bytes 
	fileSize := fileInfo.Size() 
	fmt.Println("Size of the file:", fileSize) 
}
