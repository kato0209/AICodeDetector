package main

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"time"
)

func main() {
	svr := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		time.Sleep(time.Minute)
	}))
	time.Now()
	defer svr.Close()
	startTime := time.Now()
	fmt.Println("making request")
	http.Get(svr.URL)
	fmt.Printf("finished <extra_id_0> time.Since(startTime))
}
