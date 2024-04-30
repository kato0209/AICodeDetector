package main

import (
	"github.com/bogem/id3v2"
	"log"
)

func main() {
	// Replace this with the actual path to your MP3 file
	filename := "path/to/your/file.mp3"

	tag, err := id3v2.Open(filename, id3v2.Options{Parse: true})
	if err != nil {
		log.Fatalf("Error opening MP3 file: %s", err)
	}
	defer tag.Close()

	// Update metadata
	tag.SetTitle("New Title")
	tag.SetArtist("New Artist")
	tag.SetAlbum("New Album")

	// Save changes
	if err = tag.Save(); err != nil {
		log.Fatalf("Error saving changes to MP3 file: %s", err)
	}

	fmt.Println("Playlist has been updated successfully.")
}
