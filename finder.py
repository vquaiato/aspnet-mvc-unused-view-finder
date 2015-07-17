import sys
import os

LOOKUP_EXTENSIONS = [".cshtml", ".gif", ".jpg", ".png", ".js", ".css"]
FILES_TO_SEARCH = [".cshtml", ".cs", ".css", ".less", ".js"]

FILES = []

def main(argv):
	directory = argv[0]

	files_to_look_for = load_files_in_directory(directory)

	print_break()
	print("Loading files...")
	print_break()

	print("files to look for: {0}".format(len(files_to_look_for)))
	print_break()

	print("Looking for unused files...")
	print_break()

	results = {'using': [], 'not_using': []}

	for file_name in files_to_look_for:
		references = find_references_for_file(directory, file_name)

		if references:
			results['using'].append(file_name)
		else:
			results['not_using'].append(file_name)

	print("USING: {0} files".format(len(results['using'])))
	print("NOT USING: {0} files".format(len(results['not_using'])))
	for file in results['not_using']:
		print(file)

def print_break():
	print("-" * 45)

def prepare_file_name_to_look_for(file_name):
	if ".cshtml" in file_name:
		return file_name.replace(".cshtml", "")

	return file_name

def find_references_for_file(directory, file_name):
	using = []

	for file in FILES:
		with open(file, 'r', encoding="ISO-8859-1") as searchfile:
			content = searchfile.read()
			if prepare_file_name_to_look_for(file_name) in content:
				using.append(file_name)

	return using

def load_files_in_directory(directory):
	files_to_search_for = []

	desired_extensions = list(set(LOOKUP_EXTENSIONS + FILES_TO_SEARCH))

	for root, directories, files in os.walk(directory):
		for filename in [f for f in files]:
			file_ext = ".{0}".format(filename.split(".")[-1])

			if file_ext in desired_extensions:
				FILES.append(os.path.join(root, filename))
			if file_ext in LOOKUP_EXTENSIONS:
				files_to_search_for.append(filename)

	return files_to_search_for

if __name__ == "__main__":
	if len(sys.argv) == 1:
		sys.exit("Argument required: application path")

	main(sys.argv[1:])
