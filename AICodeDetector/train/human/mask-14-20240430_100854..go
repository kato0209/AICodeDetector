<extra_id_0> (
	"io/ioutil"
	"log"
	"fmt"
	"os"
)

func AppendFile() {		
	file, err := <extra_id_1> 0644)
	if err != nil {
		log.Fatalf("failed opening file: %s", err)
	}
	defer file.Close()

	len, err <extra_id_2> The Go language was conceived in September 2007 by <extra_id_3> Rob Pike, and Ken Thompson at Google.")
	if err != nil {
		log.Fatalf("failed writing to file: %s", err)
	}
	fmt.Printf("\nLength: %d bytes", len)
	fmt.Printf("\nFile Name: %s", file.Name())
}

func ReadFile() <extra_id_4> := ioutil.ReadFile("test.txt")
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	fmt.Printf("\nLength: %d bytes", len(data))
	fmt.Printf("\nData: %s", <extra_id_5> err)
}

func main() {
	fmt.Printf("######## Append file #########\n")
	AppendFile()
	
	fmt.Printf("\n\n######## Read file #########\n")
	ReadFile()
}
