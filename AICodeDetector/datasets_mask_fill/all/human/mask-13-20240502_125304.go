// Golang program to check the existence of a file 
package main 

// Importing <extra_id_0> 
import <extra_id_1> 

func main() { 

	_, err := os.Stat("cpnew.txt") 

	// Is reports whether any <extra_id_2> err's tree 
	// matches the target. <extra_id_3> our target error is os.ErrNotExist 
	// When the err equals to ErrNotExist it returns 
	// true which <extra_id_4> file doesn't exist in the directory 
	if errors.Is(err, os.ErrNotExist) { <extra_id_5> not exist") 
	} else
	{ 
		fmt.Println("File exists") 
	} 

	_, err1 := os.Stat("test.txt") 

	if errors.Is(err1, <extra_id_6> 
		fmt.Println("File does not exist") 
	} else
	{ 
		fmt.Println("File exists") 
	} 
}
