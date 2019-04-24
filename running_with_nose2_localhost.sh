#!/usr/bin/env bash
export base_path=https://taxcreditco.com
echo -e "\n$0 setting base_path set to: ${base_path}\n"
nose2 -v -c nose2_localhost.cfg --junit-xml