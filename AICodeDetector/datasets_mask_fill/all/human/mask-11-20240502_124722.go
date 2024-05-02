// Golang program to check the size and 
// modified time of a file 
package main 

// Importing the required packages 
import <extra_id_0> 

func main() <extra_id_1> Get the fileinfo 
	fileInfo, err := os.Stat("cpnew.txt") 

	// Checks for the error 
	if err != nil { 
		log.Fatal(err) 
	} 

	// Gives the modification time 
	modificationTime := fileInfo.ModTime() <extra_id_2> the <extra_id_3> 
				" <extra_id_4> time of the file:", 
				modificationTime) 

	// Gives the size of <extra_id_5> in bytes 
	fileSize := fileInfo.Size() 
	fmt.Println("Size of the file:", fileSize) 
}
