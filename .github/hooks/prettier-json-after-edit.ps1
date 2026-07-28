$ErrorActionPreference = 'Stop'
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new($false)

try {
    $hookInput = [Console]::In.ReadToEnd() | ConvertFrom-Json
    $filePaths = @($hookInput.tool_input.filePath)

    if ($hookInput.tool_name -eq 'apply_patch') {
        $patchInput = [string]$hookInput.tool_input.input
        $filePaths += [regex]::Matches($patchInput, '(?m)^\*\*\* Update File: (.+?)\s*$') |
            ForEach-Object { $_.Groups[1].Value.Trim() }
    }

    $jsonFilePaths = $filePaths |
        Where-Object { -not [string]::IsNullOrWhiteSpace($_) -and [IO.Path]::GetExtension($_) -eq '.json' } |
        Select-Object -Unique

    foreach ($filePath in $jsonFilePaths) {
        & npx.cmd --yes prettier@3 --write -- $filePath | Out-Null

        if ($LASTEXITCODE -ne 0) {
            throw "Prettier exited with code $LASTEXITCODE."
        }
    }
}
catch {
    @{ systemMessage = "Prettier failed: $filePath - $($_.Exception.Message)" } | ConvertTo-Json -Compress
    exit 1
}