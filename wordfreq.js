const fs = require('fs');

const filePaths = ['cipher.txt', 'text1.txt', 'text2.txt'];

function removeUnwanted(content) {
    const removeNumPattern = /[0-9]/g;
    let reqText = content.replace(/[\W_]+/g, '').toUpperCase();
    reqText = reqText.replace(removeNumPattern, '');

    return reqText;
}

function wordCount(reqText) {
    const wordFreq = new Map();
    for (const word of reqText) {
        wordFreq.set(word, (wordFreq.get(word) || 0) + 1);
    }

    // Sorting results
    const sortedRes = [...wordFreq.entries()].sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0].localeCompare(b[0]);
    });

    return sortedRes;
}

function processFile(filePath) {
    const content = fs.readFileSync(filePath, 'utf8');
    const modifiedText = removeUnwanted(content);
    const wordFrequency = wordCount(modifiedText);

    console.log(`For file: '${filePath}' - `);

    for (const [word, freq] of wordFrequency) {
        console.log(`${word}: ${freq}`);
    }

    console.log();
}

// Iterating through the files
for (const filePath of filePaths) {
    processFile(filePath);
}
