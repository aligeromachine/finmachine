#!/bin/bash

cd "../back"
raw_slov="data/static/index.html"
work_slov="money_app/src/templates/index.html"


if [ -f $raw_slov ]; then
    
    rm -rf $work_slov
    mv $raw_slov $work_slov

else
    echo "NOT EXIST $raw_slov"
fi