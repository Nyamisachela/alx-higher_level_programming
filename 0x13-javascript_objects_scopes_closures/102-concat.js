// Load the required modules
const fs = require('fs');

// Function to concatenate two files
function concatFiles (source1, source2, destination) {
  // Read the first source file
  fs.readFile(source1, 'utf8', function (err, data1) {
    if (err) {
      return console.log(`Error reading ${source1}: ${err}`);
    }

    // Read the second source file
    fs.readFile(source2, 'utf8', function (err, data2) {
      if (err) {
        return console.log(`Error reading ${source2}: ${err}`);
      }

      // Concatenate data1 and data2
      const combinedData = data1 + '\n' + data2;

      // Write the combined data to the destination file
      fs.writeFile(destination, combinedData, 'utf8', function (err) {
        if (err) {
          return console.log(`Error writing to ${destination}: ${err}`);
        }

        console.log(`Files have been concatenated and saved to ${destination}`);
      });
    });
  });
}

// Command-line arguments for file paths
const [source1, source2, destination] = process.argv.slice(2);

// Call the function with provided file paths
concatFiles(source1, source2, destination);
