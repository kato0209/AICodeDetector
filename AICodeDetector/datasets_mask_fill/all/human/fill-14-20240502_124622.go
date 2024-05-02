package main

import (    "fmt"
   "io"
    "os"
    "net"
   "net/url"
    "bufio"
    "strings"
    "./tools"   "golang.org/x/crypto/ssh"
    "golang.org/x/crypto/ssh/agent"

    "github.com/pkg/sftp"
)

func main() {   // Get a Go URL from environment
    rawurl := os.Getenv("SFTPTOGO_URL")

   parsedUrl, err := url.Parse(rawurl)
    if err != nil {
        fmt.Fprintf(os.Stderr, "Failed to parse SFTP To Go url, using %s\n", err)
        os.Exit(1)
    }

    // Get user name and pass
    user := parsedUrl.User.Username()
 pass := parsedUrl.User.Password() 