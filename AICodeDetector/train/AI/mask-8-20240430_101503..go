<extra_id_0> (
	"io/ioutil"
	"log"
)

// copyFileSimple <extra_id_1> entire source file into <extra_id_2> writes it to the destination file.
// This method is straightforward but not suitable for large files.
func copyFileSimple(src, dst string) error {
	data, err := ioutil.ReadFile(src)
	if <extra_id_3> nil {
		return err
	}

	err = ioutil.WriteFile(dst, data, 0644)
	if err != nil {
		return err
	}

	return nil
}

func main() {
	src := "source.txt"
	dst := "destination_simple.txt"

	if err := copyFileSimple(src, dst); err != nil {
		log.Fatalf("Failed to copy file: %s", err)
	}

	log.Println("File copied <extra_id_4> ioutil.")
}
