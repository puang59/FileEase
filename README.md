<p align="left">
  <img src="media/logo.png" alt="FileEase Logo" width="600">
</p>

<hr>

FileEase is a command-line tool designed to simplify the organization of your files. It effortlessly sorts your files based on keywords and extensions, ensuring your digital workspace is tidy and efficient. FileEase also helps you to encrypt and compress your files easily from your command line.

<p align="left">
  <img src="media/preview.png" alt="preview" width="500">
</p>

Video Demo: https://youtu.be/AwcSrI3sijQ?si=2f3wi8B29QBmd5aV

## Overview
This project consists of main `fileease.py` file which loads all the modules from `/modules` folder like managing, encryption, compression etc
Here is short overview about each modules: 

- _managing.py
<br><br> 
This script employs the click library to create a streamlined command-line interface (CLI) for user interaction. It leverages Python's standard libraries such as os for file and directory operations and shutil for file movements. The script employs a structured approach: it first allows users to select a directory for organization, then presents choices for categorizing files based on either keywords or extensions. For each categorization method, users have the flexibility to either organize files directly in the chosen directory or encapsulate them within a designated "Master Folder". This logic ensures a systematic and customizable file organization process.

- _encrypt.py
<br><br>
This script is designed to encrypt files within a specified directory using the Fernet symmetric encryption provided by the `cryptography` library. The script begins by prompting the user to select a directory containing the file they wish to encrypt. Once a directory is chosen and validated, the script lists the files within that directory. The user is then prompted to select a file for encryption, which is read into memory and encrypted using the Fernet key. The encrypted data is subsequently saved as a new file with a ".enc" extension. Notably, the script also provides an option to store the encryption key for future reference in a `keys.txt` file, complete with metadata such as the filename and the timestamp of the encryption. Overall, with a user-friendly CLI interface powered by the `click` library, the script offers a straightforward and secure method for file encryption while ensuring that users have the option to manage and store their encryption keys.

- _decrypt.py
<br><br>
This script serves as a counterpart to the previous encryption script, focusing on the decryption process. Utilizing the `cryptography` library's Fernet symmetric encryption mechanism, the script prompts the user to select a directory containing the encrypted file they wish to decrypt. After directory validation, the script displays the available encrypted files for user selection. Upon selecting a file, the user is prompted to provide the corresponding encryption key. Using this key, the script decrypts the selected file and saves the decrypted content with a ".dec" extension in the same directory. The user is then informed of the successful decryption operation. Overall, this script provides a streamlined CLI interface using the `click` library, offering users a straightforward method to decrypt their files securely.

- _compress.py
<br><br>
This script focuses on compressing files and directories into a ZIP archive. Leveraging Python's built-in `zipfile` library, the script initiates by prompting the user to specify a directory containing the files they wish to compress. After directory validation and listing the available files, the user is prompted to provide a name for the resulting ZIP archive and the desired storage location. Utilizing this information, the script then creates a ZIP archive, adding each file from the specified directory to the archive. The compressed ZIP file is saved at the specified location. Employing the `click` library for a user-friendly CLI interface, the script streamlines the file compression process, ensuring that users can easily package their files and directories into a single, organized ZIP archive.

- _extract.py
<br><br>
This script is tailored for extracting files from a specified ZIP archive. Utilizing Python's standard `zipfile` library, the script initiates by prompting the user to provide the path to the ZIP archive they intend to extract. After validating the existence of the provided ZIP file path, the script prompts the user to specify a directory where the extracted files should be placed. If the directory doesn't exist, the script creates it. Subsequently, using the `extractall()` method from the `zipfile` library, the script efficiently extracts all contents of the specified ZIP archive into the designated directory. The `click` library further enhances user interaction by offering a clear and intuitive CLI interface, guiding users through the extraction process and ensuring a seamless experience.

## Features

### Manage Files
- **Keyword-Based Organization:** FileEase automatically creates folders with specified keywords and moves files containing those keywords in their names to the respective folders. For example, if you have files with "screenshot" in their names, FileEase will create a "screenshot" folder and neatly organize them for you.
  ![Keyword Mode Screenshot](media/keyword.png)

- **Extension-Based Sorting:** If you prefer to sort files by their extensions, FileEase can create folders for different file extensions and categorize your files accordingly. For instance, all your PNG files will be grouped together in a "png" folder, while MOV files will have their own "mov" folder.
  ![Extension Mode Screenshot](media/manage.png)

### Encryption & Decryption
- **File Encryption:** FileEase effortlessly secures files, whether they're PDFs, PPTX, or images, providing an encryption key for secure storage in keys.txt, ensuring easy decryption when needed.
  ![Encryption Screenshot](media/encrypt.png)

- **File Decryption:** FilEase can decrypt any type of file if a valid key is provided
  ![Decrypt Screenshot](media/decrypt.png)

### Compress & Extract
- **File Compression:** Filease ease can effortlessly compress your files and folders right from your command line.
    ![Compress Screenshot](media/compress.png)

- **File Extraction:** Filease ease can effortlessly extract your files and folders right from your command line.
  
<hr>

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/puang59/FileEase.git
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run FileEase**:
   ```bash
   python fileease.py
   ```

## Contribute

We welcome contributions from the open-source community. Feel free to [fork this repository](https://github.com/puang59/FileEase/fork) and submit pull requests to help improve FileEase.

## License

This project is open-source under the [MIT License](LICENSE). While you're free to view, use, and contribute to the code, please refrain from distributing it as your own. 
<br><br>
Made with ❤️ by Karan 
