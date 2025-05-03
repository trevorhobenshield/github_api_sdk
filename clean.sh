#!/usr/bin/bash

if [ -d 'dist' ] ; then
    rm -r dist
fi
if [ -d 'build' ] ; then
    rm -r build
fi
if [ -d 'github_api_sdk.egg-info' ] ; then
    rm -r github_api_sdk.egg-info
fi