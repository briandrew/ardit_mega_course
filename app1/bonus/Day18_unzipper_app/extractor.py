import zipfile


def extract_archive(archive_path, destination_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_dir)


if __name__ == "__main__":
    extract_archive(archive_path="compressed.zip", destination_dir="destination")
