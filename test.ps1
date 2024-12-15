<#
Usage:
.\test.ps1
#>

# Clear screen
Clear-Host

# Activate the virtual environment
& .\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run project
python test

deactivate
