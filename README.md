# introduction
The tools checks if an updated version of a module follows
the rules defined in Section 10 of RFC 6020 and Section 11 of RFC 7950 or 
huawei rules or the third-paryt rules(enriching).then it also can used as Version 
Difference Generation Tool,can used to generate data nodes adding, deleting, and 
modifying  results.


# installation:
python setup.py install 
# yang-compatibility-check illustration:
python yang-compatibility-check -p $new_path -P $old_path --check-update-from=$old_files $new_files
# yang-schema-compare illustration:
python yang-compatibility-check --deviation-module=$new_deviation_files.yang --check-update-from=$old_files $new_files
# Backwards Compatibility Issues:
It should be noted that some of the modules released in huawei may break the backwards compatibility guidelines defined in RFC 6020 when compared to the same modules released in huawei_N+1. This is because the "native" YANG modules for huawei are generated from internal schema files that are an integral part of the implementation, and, as such, these can change in ways that break backwards compatibility per RFC 6020/7950 guidelines when new features are introduced or when bugs are fixed. Thus, while we rigorously review the changes that impact the external YANG schema, Huawei cannot guarantee full backwards compatibility of these modules across releases.

However, when new versions of the native models are released, the check-models.sh script, in conjunction with pyang, can be used to determine what technically non-compatible changes may have occurred. Please run check.sh from this directory with pyang 2.5 or greater on your path thus:

$ ./check-models.sh -b 8.21.0
The script will check basic compilation using pyang (some open modules will be reported missing unless you include them on your pyang module path) and then run backwards compatibility checks against the model in the ../8.20.10 directory. 
