package main

import (
	"fmt"
	"immortal/dotfiles"
)

func main() {
	value, err := dotfiles.Getfiles("./")
	if err != nil {
		fmt.Printf("There was an error")
	}
	for _, file := range value {
		fmt.Printf("%s\n", file.Name())
	}
}
