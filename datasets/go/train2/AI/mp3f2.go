package main

import (
	"fmt"
	"github.com/bogem/id3v2"
	"log"
)

func main() {
	// Replace 'path/to/your/file.mp3' with the actual path to your MP3 file
	filename := "path/to/your/file.mp3"

	tag, err := id3v2.Open(filename, id3v2.Options{Parse: true})
	if err != nil {
		log.Fatalf("Error opening MP3 file: %s", err)
	}
	defer tag.Close()

	title := tag.Title()
	artist := tag.Artist()
	album := tag.Album()

	fmt.Printf("Title: %s\nArtist: %s\nAlbum: %s\n", title, artist, album)
}
