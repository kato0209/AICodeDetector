
package <extra_id_0> copyFile(src, dst string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return <extra_id_1> err <extra_id_2> err != nil {
		return err
	}
	defer destinationFile.Close()

	_, err = io.Copy(destinationFile, sourceFile)
	return err
}

func main() {
	err := copyFile("source.txt", "destination.txt")
	if err != nil {
		panic(err)
	}
}
