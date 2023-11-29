# The transitions between Windows and Unix shell

The table below shows the issue of using Windows tools - i.e. you have to "relearn" either way you go.

## Tool Comparison Table

| Unix/Bash Tool       | Functionality             | Windows Equivalent or Alternative                             | Notes                 |
| -------------------- | ------------------------- | ------------------------------------------------------------- | --------------------- |
| `ls`                 | List directory contents   | `dir`                                                         |                       |
| `cd`                 | Change directory          | `cd`                                                          |                       |
| `mv`                 | Move/rename files         | `move`, `rename`                                              |                       |
| `cp`                 | Copy files                | `copy`, `xcopy`, `robocopy`                                   |                       |
| `rm`                 | Remove files/directories  | `del`, `rmdir`                                                |                       |
| `touch`              | Create empty files        | `copy con`, `New-Item` (PowerShell)                           |                       |
| `grep`               | Text search               | `findstr`                                                     |                       |
| `awk`                | Text processing           | `findstr`, PowerShell cmdlets                                 | More advanced in Unix |
| `sed`                | Stream editor             | PowerShell cmdlets                                            | More advanced in Unix |
| `chmod`              | Change file permissions   | `icacls`, `attrib`                                            |                       |
| `chown`              | Change file ownership     | `takeown`                                                     |                       |
| `ps`                 | List running processes    | `tasklist`, `Get-Process` (PowerShell)                        |                       |
| `kill`               | Terminate processes       | `taskkill`, `Stop-Process` (PowerShell)                       |                       |
| `df`                 | Disk space usage          | `dir`, `Get-Volume` (PowerShell)                              |                       |
| `du`                 | Estimate file space usage | `dir /s`, `Get-ChildItem` (PowerShell)                        |                       |
| `top`/`htop`         | System monitor            | `Task Manager`, `Get-Process` (PowerShell)                    |                       |
| `curl`               | Data transfer             | `curl` (in newer versions), `Invoke-WebRequest` (PowerShell)  |                       |
| `ssh`                | Secure Shell              | `ssh` (in newer versions), `Putty`                            |                       |
| `tar`                | Archive tool              | `Compress-Archive` (PowerShell), WinRAR, 7-Zip                |                       |
| `cron`               | Task scheduler            | `Task Scheduler`, `schtasks`                                  |                       |
| `nano`/`vim`/`emacs` | Text editors              | `Notepad`, `VSCode`, `Get-Content`/`Set-Content` (PowerShell) |                       |
