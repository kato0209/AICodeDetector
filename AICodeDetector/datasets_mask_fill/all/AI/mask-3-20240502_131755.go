
package main

import <extra_id_0> {
	fileInfo, err := os.Stat("yourfilename.ext")
	if err != nil {
		fmt.Println(err)
		return
	}

	modTime := fileInfo.ModTime()
	fmt.Println("Last modified time:", modTime.Format(time.RFC1123))
}
