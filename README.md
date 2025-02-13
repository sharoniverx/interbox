# InterBox

InterBox is a Python-based application that provides a powerful alternative to the default uninstall function on Windows, offering enhanced deep-cleaning capabilities to ensure complete removal of unwanted software.

## Features

- **List Installed Software**: Displays a list of all software currently installed on your Windows system.
- **Uninstall Software**: Enables you to uninstall software via the Windows Management Instrumentation Command-line (WMIC).
- **Deep Clean**: After uninstallation, InterBox attempts to remove any residual files and folders associated with the software from common directories such as Program Files and AppData.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/interbox.git
   ```
2. Navigate to the project directory:
   ```bash
   cd interbox
   ```

## Usage

1. Run the script:
   ```bash
   python interbox.py
   ```
2. The program will list all the installed software.
3. Enter the name of the software you wish to uninstall when prompted.
4. InterBox will proceed to uninstall the software and perform a deep clean of any residual files.

## Important Notes

- Administrator privileges may be required to uninstall certain software or delete protected system directories.
- The deep clean process attempts to remove known directories associated with the software but may need customization depending on the software's install paths.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or file an issue for any bugs or features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.