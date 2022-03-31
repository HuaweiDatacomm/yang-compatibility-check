# yang-compatibility-check illustration:
python yang-compatibility-check -p $new_path -P $old_path --check-update-from=$old_files $new_files
# yang-schema-compare illustration:
python yang-compatibility-check --deviation-module=$new_deviation_files.yang --check-update-from=$old_files $new_files
