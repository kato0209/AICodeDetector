// Golang program to check the size and 
// modified time of a file 
package main 

// Importing the <extra_id_0> 
import ( 
	"fmt"
	"log"
	"os"
) 

func main() { <extra_id_1> the fileinfo 
	fileInfo, err := os.Stat("cpnew.txt") <extra_id_2> for the error 
	if err != nil { 
		log.Fatal(err) 
	} 

	// Gives the modification <extra_id_3> := fileInfo.ModTime() 
	fmt.Println("Name of the file:", fileInfo.Name(), 
				" Last <extra_id_4> of the file:", 
				modificationTime) 

	// Gives the <extra_id_5> the file in bytes 
	fileSize := fileInfo.Size() 
	fmt.Println("Size of the file:", fileSize) 
}
