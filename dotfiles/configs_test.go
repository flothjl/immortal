package dotfiles

import (
	"encoding/json"
	"testing"
)

// TestConfigs tests unmarshalling config json object into structs.
func TestConfigs(t *testing.T) {
	testConfig := `{
		"exportPath":"~/Documents/test_export",
		"shell":"zsh",
		"files":[
			{
				"name":"FileType1",
				"path":".",
				"fileNames": [
					"file1.txt",
					"file1.sh"
				]
			},
			{
				"name":"FileType2",
				"path":".",
				"fileNames": [
					"file2.txt",
					"file2.sh"
				]
			}
		]
	}`
	var configs Config
	json.Unmarshal([]byte(testConfig), &configs)
	want := 2
	if len(configs.Files) != want {
		t.Fatalf(`Length of files: %d \nWanted length: %d`, len(configs.Files), want)
	}
}

func TestExportConfigs(t *testing.T) {
	in := `{
		"exportPath":"/Users/joshuafloth/Developer/immortal/dotfiles/dotfiles_test/export_test",
		"shell":"zsh",
		"files":[
			{
				"path":"/Users/joshuafloth/.dotfiles/.aliases",
				"fileNames": [
					".aliases",
				]
			}
		]
	}`

	var configs Config
	json.Unmarshal([]byte(in), &configs)
	err := ExportConfigs(configs)
	if err != nil {
		t.Fatalf("Unsuccessful export of dotfiles. Error: %s", err)
	}

}

func TestGetFiles(t *testing.T) {
	path := "./dotfiles_test"
	results, err := Getfiles(path)
	if err != nil {
		t.Fatalf("Error getting dotfiles: %s", err)
	}
	pass := false
	want := ".test1"
	for _, file := range results {
		if file.Name() == want {
			pass = true
		}
	}
	if !pass {
		t.Fatalf("Expected file: %s. File does not exist", want)
	}
}

// TestHelloName calls greetings.Hello with a name, checking
// for a valid return value.
// func TestHelloName(t *testing.T) {
// 	name := "Gladys"
// 	want := regexp.MustCompile(`\b` + name + `\b`)
// 	msg, err := Hello("Gladys")
// 	if !want.MatchString(msg) || err != nil {
// 		t.Fatalf(`Hello("Gladys") = %q, %v, want match for %#q, nil`, msg, err, want)
// 	}
// }

// TestHelloEmpty calls greetings.Hello with an empty string,
// checking for an error.
// func TestHelloEmpty(t *testing.T) {
// 	msg, err := Hello("")
// 	if msg != "" || err == nil {
// 		t.Fatalf(`Hello("") = %q, %v, want "", error`, msg, err)
// 	}
// }
