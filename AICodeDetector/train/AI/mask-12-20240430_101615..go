package main

import (
	"fmt"
	"github.com/bogem/id3v2"
	"log"
)

func main() {
	// Replace 'path/to/your/file.mp3' with the actual path to your MP3 file
	filename <extra_id_0> err := id3v2.Open(filename, id3v2.Options{Parse: true})
	if err != <extra_id_1> opening MP3 file: %s", err)
	}
	defer tag.Close()

	title <extra_id_2> := tag.Artist()
	album := tag.Album()

	fmt.Printf("Title: %s\nArtist: %s\nAlbum: %s\n", title, artist, album)
}
