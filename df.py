import pytsk3

# Function to recursively process directory entries
def process_directory(directory, parent_path=''):
    for entry in directory:
        if entry.info.name.name.decode('utf-8') in [".", ".."]:
            continue

        # Construct the full path of the entry
        path = '/{}/{}'.format(parent_path, entry.info.name.name.decode('utf-8'))

        # Print metadata information of the entry
        print("File: {}".format(path))
        print("Size: {}".format(entry.info.meta.size))
        print("Type: {}".format(entry.info.name.type))
        print("")

        # If the entry is a directory, recursively process its contents
        if entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            sub_directory = entry.as_directory()
            process_directory(sub_directory, path)


# Main function
def main():
    # Open the disk image file
    img_path = 'path/to/disk/image.dd'
    img = pytsk3.Img_Info(img_path)

    # Open the file system of the disk image
    fs = pytsk3.FS_Info(img)

    # Retrieve the root directory of the file system
    root_dir = fs.open_dir(path='/')

    # Process the root directory recursively
    process_directory(root_dir)

    # Close the file system and image
    fs.close()
    img.close()


if __name__ == '__main__':
    main()
