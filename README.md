# introduction
The tools checks if an updated version of a module follows
the rules defined in Section 10 of RFC 6020 and Section 11 of RFC 7950 or 
huawei rules or the third-paryt rules(enriching).then it also can used as Version 
Difference Generation Tool,can used to generate data nodes adding, deleting, and 
modifying  results.


## **Features**
- provide command line plugin for managing huawei net-engine series products and cloud-engine series switches
- provide netconf plugin for managing huawei net-engine series products and cloud-engine series switches
- provide a common command line module
- provide a template command line module for delivering commands in batches
- provide a common netconf module, it will be referenced by ansible api generated by [ansible-gen](https://github.com/HuaweiDatacomm/ansible-gen)
# installation:
python setup.py install 
# yang-compatibility-check illustration:
python yang-compatibility-check -p $new_path -P $old_path --check-update-from=$old_files $new_files
# yang-schema-compare illustration:
python yang-compatibility-check --deviation-module=$new_deviation_files.yang --check-update-from=$old_files $new_files
