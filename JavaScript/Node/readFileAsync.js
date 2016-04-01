var readFileAsync = path => new Promise((resolve, reject) => fs.readFile(path, function(error, data) {
    if (error) reject(error);
    resolve(data);
}));
