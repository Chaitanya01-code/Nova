import os
import shutil
import subprocess
import sys
import webbrowser
from typing import Any, Dict, Optional


class ApplicationLauncher:
    """Launch or prepare an external application connection.

    Supports three safe forms:
      1. a browser URL,
      2. a desktop executable name in PATH,
      3. an executable/command path on disk.
    """

    def launch(self, app_name: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        metadata = metadata or {}

        try:
            app_name_lc = app_name.strip().lower()

            # 1) Browser URL -> browser tab
            if app_name_lc.startswith("http://") or app_name_lc.startswith("https://"):
                opened = webbrowser.open_new_tab(app_name)
                return {
                    "app": app_name,
                    "status": "launched" if opened else "failed",
                    "metadata": metadata,
                    "opened": opened,
                    "kind": "browser_url",
                }

            # 2) Local executable path or script path -> direct file opening
            executable_path = app_name
            if os.path.exists(executable_path):
                if os.name == "nt":
                    os.startfile(executable_path)
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", executable_path])
                else:
                    subprocess.Popen(["xdg-open", executable_path])

                return {
                    "app": app_name,
                    "status": "launched",
                    "metadata": metadata,
                    "opened": True,
                    "kind": "desktop_file_path",
                }

            # 3) Resolve an installed executable off the PATH
            resolved = shutil.which(app_name) or shutil.which(app_name + ".exe")
            if resolved:
                if os.name == "nt":
                    # Use Popen with list form so arguments are clean and controlled.
                    subprocess.Popen([resolved], shell=False)
                elif sys.platform == "darwin":
                    subprocess.Popen([resolved])
                else:
                    subprocess.Popen([resolved])

                return {
                    "app": app_name,
                    "status": "launched",
                    "metadata": metadata,
                    "opened": True,
                    "kind": "desktop_executable",
                    "resolved_path": resolved,
                }

            # 4) Final safe fallback: no binary found, but allow text command names like notepad, cmd
            if os.name == "nt":
                # Safe, familiar Windows apps that are common and user-requested.
                safe_windows_commands = {
                    "notepad": "notepad.exe",
                    "calc": "calc.exe",
                    "cmd": "cmd.exe",
                    "mspaint": "mspaint.exe",
                    "powershell": "powershell.exe",
                }
                target = safe_windows_commands.get(app_name.lower())
                if target:
                    subprocess.Popen([target], shell=True)
                    return {
                        "app": app_name,
                        "status": "launched",
                        "metadata": metadata,
                        "opened": True,
                        "kind": "desktop_executable",
                        "resolved_path": target,
                    }

            return {
                "app": app_name,
                "status": "failed",
                "metadata": metadata,
                "opened": False,
                "kind": "desktop_executable",
                "error": "Application executable was not found in the environment PATH or filesystem.",
            }
        except Exception as exc:
            return {
                "app": app_name,
                "status": "failed",
                "metadata": metadata,
                "error": str(exc),
                "opened": False,
                "kind": "desktop_executable",
            }
