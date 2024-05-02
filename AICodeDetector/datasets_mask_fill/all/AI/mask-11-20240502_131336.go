<extra_id_0> (
	"io/ioutil"
)

func main() {
	data := []byte("Hello, World!")
	err := ioutil.WriteFile("example.txt", data, 0644)
	if err != nil {
		panic(err)
	}
}
