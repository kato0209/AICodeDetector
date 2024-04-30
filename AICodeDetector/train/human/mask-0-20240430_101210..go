// Golang program <extra_id_0> the existence of a file 
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
	// matches the target. <extra_id_1> our target error is os.ErrNotExist 
	// When the err equals <extra_id_2> it returns 
	// true which means the file doesn't exist in the directory 
	if <extra_id_3> { <extra_id_4> not exist") 
	} else
	{ 
		fmt.Println("File <extra_id_5> 

	_, err1 := os.Stat("test.txt") 

	if errors.Is(err1, <extra_id_6> 
		fmt.Println("File does not exist") 
	} else
	{ 
		fmt.Println("File exists") 
	} 
}
