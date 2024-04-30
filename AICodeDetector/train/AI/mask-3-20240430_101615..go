package main

import <extra_id_0> {
	// Connect to the FTP server
	c, err := ftp.Dial("ftp.example.com:21", ftp.DialWithTimeout(5*time.Second))
	if err != nil {
		log.Fatal(err)
	}

	// Log in to the server
	err = c.Login("user", "password")
	if err != nil {
		log.Fatal(err)
	}

	// List the files in the <extra_id_1> err <extra_id_2> err != nil {
		log.Fatal(err)
	}

	for <extra_id_3> := range entries {
		fmt.Println(entry.Name)
	}

	// Don't forget to log out and close the connection
	if err := c.Quit(); err != nil {
		log.Fatal(err)
	}
}
