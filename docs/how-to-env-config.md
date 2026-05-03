# How-to: Manage Environments and Port Configurations

This guide provides practical steps for managing the local development environment and resolving common configuration conflicts.

## Activate the Project Environment

To ensure you are using the correct library versions and Python interpreter, always work within the scoped virtual environment.

### Windows (PowerShell)
```powershell
.\bert-classifier-env\Scripts\activate
```

### Linux / macOS
```bash
source bert-classifier-env/bin/activate
```

## Configure a Custom API Port

By default, the API service runs on port `8081` to avoid collisions with standard web services (often on `8000` or `8080`). You can override this setting using the `PORT` environment variable.

### Temporary Override (Windows PowerShell)
```powershell
$env:PORT=9000; python src/main.py
```

### Temporary Override (Linux/macOS)
```bash
PORT=9000 python src/main.py
```

## Update Project Dependencies

When a new package is required, follow this workflow to ensure the `bert-classifier-env` remains consistent.

1. **Activate** the environment as shown above.
2. **Install** the package:
   ```bash
   pip install <package-name>
   ```
3. **Verify** the installation:
   ```bash
   pip show <package-name>
   ```

## Troubleshoot Port Conflicts

If you see an error like `[Errno 10048] error while attempting to bind on address`, the port is already in use by another project.

1. **Identify the process** (Windows):
   ```powershell
   netstat -ano | findstr :8081
   ```
2. **Action**: Either kill the conflicting process or use a different port for this project as described in the "Configure a Custom API Port" section above.
