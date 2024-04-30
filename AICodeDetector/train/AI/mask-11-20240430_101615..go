package <extra_id_0> main() {
	response, err := http.Get("http://localhost:8080")
	if err != nil {
		fmt.Printf("Error making request: <extra_id_1> response.Body.Close()

	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Printf("Error reading response body: %s\n", err)
		return
	}

	fmt.Printf("Server response: %s\n", string(body))
}
