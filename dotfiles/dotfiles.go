package dotfiles

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func PrintUserDir() (string, error) {
	jsonString := `{"exportPath":"~/Documents", "shellType":"zsh"}`
	var myJson Config
	json.Unmarshal([]byte(jsonString), &myJson)
	return myJson.Shell, nil
}

func ExportConfigs(config Config) error {
	if _, err := os.Stat(config.ExportPath); os.IsNotExist(err) {
		err := os.MkdirAll(config.ExportPath, 0600)
		if err != nil {
			return err
		}
	}

	filesToExport := config.Files

	for _, file := range filesToExport {
		for _, fileName := range file.FileNames {
			err := CopyFile(file.Path, config.ExportPath, fileName)
			if err != nil {
				return err
			}
		}
	}

	return nil
}

func Getfiles(path string) ([]os.DirEntry, error) {
	files, err := os.ReadDir(path)
	if err != nil {
		log.Fatal("Error ")
		return nil, err
	}
	for _, f := range files {
		fmt.Print(f.Name())
	}
	return files, nil
}

func CopyFile(src string, dst string, filename string) error {

	srcFile, err := os.Open(filepath.Join(src, filename))

	if err != nil {
		fmt.Printf("Error reading source file: %s", err.Error())
		return err
	}

	defer srcFile.Close()

	newFile, err := os.Create(filepath.Join(dst, filename))

	if err != nil {
		fmt.Printf("Error writing file: %s", err.Error())
		return err
	}

	defer newFile.Close()

	return nil
}
