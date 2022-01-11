package dotfiles

type File struct {
	Name      string   `json:"name"`
	Path      string   `json:"path"`
	FileNames []string `json:"fileNames"`
}

type Config struct {
	ExportPath string `json:"exportPath"`
	Shell      string `json:"shell"`
	Files      []File `json:"files"`
}
