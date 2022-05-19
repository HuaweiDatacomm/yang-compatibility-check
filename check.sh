#!/bin/bash
#
# Vendor-specific check script. Assumes that pyang is on path and that
# all standard modules are on its internal module path.
#
# Deviation modules are NOT checked as they require specific imports
# typically not available locally.
#
# This script will only be run for the last release of a version branch.
# When a new set of models is committed for a version, the previous
# should be removed.
#
#
#
# Deprecating use of yanglint at least until Focal Fossa Ubuntu release
# is out.
#
#
#
platform_dir="huawei/yang/network-router"

# NOTE: please just have the directories you are checking here
to_check="8.20.0 8.20.10 8.21.0"

debug=0

checkDir () {
    if [ "$debug" -eq "1" ]; then
	echo Checking yang files in $platform_dir/$1
    fi
    exit_status=""
    cwd=`pwd`
    cd $1
    to_process=`grep -L submodule huawei-*-cfg.yang huawei-*-oper.yang huawei-sysadmin-*.yang huawei-*-deviation*.yang`
    for f in $to_process; do
	if [ "$debug" -eq "1" ]; then
	    echo Checking $f...
	fi
	errors=`pyang --lax-quote-checks $yanglint_flags $f 2>&1 | grep -v "warning:"`
	if [ ! -z "$errors" ]; then
	    printf "PYANG: Errors in $f\n"
	    printf "$errors\n"
	    exit_status="failed!"
	    # if [ "$debug" -eq "1" ]; then
	    # 	printf "\n\n*** EARLY EXIT DUE TO ERROR ***\n\n"
	    # 	exit 1
	    # fi
	fi
    done
    cd $cwd
    
    if [ ! -z "$exit_status" ]; then
       exit 1
    fi
}

if [ "$debug" -eq "1" ]; then
    printf "\nChecking modules with yanglint, using 'lax quote checks' via perlre filtering\n"
fi

if [ -e "$platform_dir" ]; then
    cd $platform_dir
fi

# for d in $to_check; do
#     checkDir $d
# done

declare -a pids
for d in $to_check; do
    (checkDir $d) &
    pids+=("$!")
done

for p in $pids; do
    wait $p || exit 1
done
