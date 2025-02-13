import os
import subprocess
import shutil
from winreg import OpenKey, EnumKey, QueryValueEx, HKEY_LOCAL_MACHINE, KEY_READ

class InterBox:
    def __init__(self):
        self.installed_software = []

    def get_installed_software(self):
        try:
            path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
            with OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_READ) as key:
                for i in range(1024):
                    try:
                        subkey_name = EnumKey(key, i)
                        with OpenKey(key, subkey_name) as subkey:
                            software_name, _ = QueryValueEx(subkey, "DisplayName")
                            self.installed_software.append(software_name)
                    except EnvironmentError:
                        break
        except Exception as e:
            print(f"Failed to retrieve installed software: {e}")

    def display_installed_software(self):
        if self.installed_software:
            print("Installed Software:")
            for index, software in enumerate(self.installed_software, start=1):
                print(f"{index}. {software}")
        else:
            print("No installed software found.")

    def uninstall_software(self, software_name):
        try:
            uninstall_process = subprocess.check_call(['wmic', 'product', 'where', f'name="{software_name}"', 'call', 'uninstall'])
            if uninstall_process == 0:
                print(f"Successfully uninstalled {software_name}")
                self.deep_clean(software_name)
            else:
                print(f"Failed to uninstall {software_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error during uninstallation: {e}")

    def deep_clean(self, software_name):
        print(f"Performing deep clean for {software_name}...")

        # Example paths that might need cleaning (user may need to customize)
        paths_to_clean = [
            os.path.join(os.environ['PROGRAMFILES'], software_name),
            os.path.join(os.environ['PROGRAMFILES(X86)'], software_name),
            os.path.join(os.environ['APPDATA'], software_name),
            os.path.join(os.environ['LOCALAPPDATA'], software_name)
        ]

        for path in paths_to_clean:
            try:
                if os.path.exists(path):
                    shutil.rmtree(path)
                    print(f"Removed directory: {path}")
            except Exception as e:
                print(f"Failed to remove directory {path}: {e}")

    def run(self):
        self.get_installed_software()
        self.display_installed_software()
        choice = input("Enter the name of the software you wish to uninstall: ").strip()
        if choice in self.installed_software:
            self.uninstall_software(choice)
        else:
            print("Software not found in the list.")

if __name__ == "__main__":
    interbox = InterBox()
    interbox.run()