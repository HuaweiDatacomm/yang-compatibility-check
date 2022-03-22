# yang-compatibility-check illustration:
python pyang -p $new_path -P $old_path --check-update-from=$old_files $new_files
# yang-schema compare illustration:
python pyang --deviation-module=$new_deviation_files.yang --check-update-from=$old_files $new_files
