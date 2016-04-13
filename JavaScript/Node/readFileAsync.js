var readFileAsync = path => new Promise((resolve, reject) => fs.readFile(path, (error, data) => {
    if (error) reject(error);
    resolve(data);
}));
