### Installing ConEmu

Check apps installed:
```
scoop list
```

Check if there is `extras` bucket:
```
scoop bucket list
```

If not add it & then install conemu:
```
scoop bucket add extras
scoop install conemu
```

Milan's ConEmu settings file, as promised

1. Extract archive to some directory (see attached)
2. Edit the XML file by replacing %TargetDir% with name of the directory where you extracted the archive in previous step 1
3. Edit the shortcut by replacing %TargetDir% with name of the directory where you extracted the archive in previous step (you can also "change icon" and point to the icon in the extracted directory) (edited)
