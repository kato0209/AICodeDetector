// Golang program to check the existence of a file 
package main 

// Importing required packages 
import ( 
	"errors"
	"fmt"
	"os"
) 

func main() { 

	_, err := os.Stat("cpnew.txt") 

	// Is reports whether any error in err's tree 
	// matches the target. 
	// Here our target error is os.ErrNotExist 
	// When the err equals to ErrNotExist it returns 
	// true which means the file doesn't exist in the directory 
	if errors.Is(err, os.ErrNotExist) { 
		fmt.Println("File does not exist") 
	} else
	{ 
		fmt.Println("File exists") 
	} 

	_, err1 := os.Stat("test.txt") 

	if errors.Is(err1, os.ErrNotExist) { 
		fmt.Println("File does not exist") 
	} else
	{ 
		fmt.Println("File exists") 
	} 
}
