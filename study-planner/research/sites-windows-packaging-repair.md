# Windows Sites packaging compatibility repair — 17 October 2026

The installed Sites 1.0.1 source workflow reached packaging successfully but the system `bash` selected WSL. Passing Windows drive paths through that shell failed. Selecting Git Bash alone exposed a second issue: GNU tar interpreted a `C:/...` archive destination as a remote-host path.

The local installed helper `scripts/package-site.mjs` now selects the observed Git Bash installation on Windows and converts Windows absolute paths to Git Bash drive paths. It continues to invoke the bundled shell packager and its original validation and metrics. Non-Windows behavior is unchanged. No authentication token is written to this note or the repository.

```javascript
import { fileURLToPath } from "node:url";
import { runMeasuredCommand } from "./workflow-metrics.mjs";

const windows = process.platform === "win32";
const portablePath = (value) => windows
  ? value.replaceAll("\\", "/").replace(/^([A-Za-z]):\//, (_, drive) => `/${drive.toLowerCase()}/`)
  : value;
await runMeasuredCommand([
  windows ? "C:/Program Files/Git/bin/bash.exe" : "bash",
  portablePath(fileURLToPath(new URL("../skills/sites/scripts/package-site.sh", import.meta.url))),
  ...process.argv.slice(2).map(portablePath),
]);
```

Validation: the official workflow pushed and verified source `f4195fd9c5a874cf3f032b4724f293a94168e5f1`, packaged the declared static output, and native private publication returned success for version 107. Its archive contained 531 files after server ingestion. This is a local compatibility repair; a plugin update may replace it.
