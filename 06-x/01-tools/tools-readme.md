# Tools

## Targets

- Cross-platform development
- Create increasingly good habits (learn new tool if needed)

## Editors

- VS code - try to optimize use of it
- Add extensions - Harpoon, etc
- NeoVim

## Terminal

- learn Powershell
  - debugging of scripts
- Bash (or WSL on Windows)

### Windows Subsystem for Windows

Installing WSL (Windows Subsystem for Linux) involves a few steps, mostly executed in PowerShell. Here's a simplified guide:

1. **Enable the WSL feature**: Open PowerShell as an administrator and run:

   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```

2. **Enable Virtual Machine feature**: Still in PowerShell, execute:

   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

3. **Restart your computer**.

4. **Download Linux Kernel Update Package**: Go to the Microsoft website and download the WSL2 Linux Kernel update package. Follow the installation instructions.

5. **Set WSL2 as your default version**: Open PowerShell and run:

   ```powershell
   wsl --set-default-version 2
   ```

6. **Install a Linux Distro**: Open Microsoft Store, search for a Linux distribution like Ubuntu, and install it.

7. **Initialize Distro**: Once installed, launch the distro from the Start menu and follow on-screen instructions to complete the setup.

8. **Check Installation**: Open a new PowerShell window and run `wsl -l -v` to see the installed distro and ensure it's using WSL2.

9. **Set up in VS Code**: If you have VS Code, you can now set WSL as the default terminal as described in the previous answer.

This should get you up and running with WSL on your Windows machine.

## Git

- Use it in VS code
- Use Github desktop
- Use git from terminal
