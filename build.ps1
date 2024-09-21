$project = "modelquery"
micromamba create -n $project "python<3.12"
micromamba activate $project

pip install -e .
pip install pyinstaller

$HIDDEN_OPT = '--collect-all=fastexcel'
$CLEAN_OPT = '--clean', '--noconfirm'
$HIDE_WINDOW = '--noconsole'

pyinstaller $HIDE_WINDOW --optimize 2 $HIDDEN_OPT -D -n hkf-cli @CLEAN_OPT src/$project/__main__.py

# Optional, comment this to debug pyinstaller spec.
Remove-Item *.spec
# Clean build cache directory
Remove-Item -Recurse -Force build\
