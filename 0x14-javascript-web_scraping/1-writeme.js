#!/usr/bin/node

// Writes to a file
const fs = require('fs')

if (process.argv.length === 4) {
    fileName = process.argv[2]
    data = process.argv[3]
    fs.writeFile(fileName, data, (err) => {
        if (err)
            console.log(err)
    })
   
}
